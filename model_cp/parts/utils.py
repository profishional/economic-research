import pandas as pd
import numpy as np
from pathlib import Path

"""
    The Cherry Picker (CP) calculation process for the CP agent.
    Based on the Portal-API CP in pokt-foundation github.
"""

# TODO logs; service, failure, error

# relative path of where all the data should be
PATH = str(Path().parent.resolve().parent.resolve()) + '/data/'
TIMEOUT_LIMIT = 20
TIMEOUT_VARIANCE = 2

def unsortedList(filename="rawServiceLog.csv") -> pd.DataFrame:
    # reads: id, attempts, successStatuses, medianSuccessLatency, weightedSuccessLatency, failure
    # TODO record failure, erase if successful

    df = pd.read_csv(PATH + filename)

    df['successRate'] = np.round(df['successStatus']/ df['attempts'],5)
    df['medianSuccessLatency'] = np.round(df['medianSuccessLatency'],5)
    df['weightedSuccessLatency'] = np.round(df['weightedSuccessLatency'],5)

    return df


def sortItems(itemsList: pd.DataFrame) -> pd.DataFrame:
    # sort on the precalculated number of weighted success
    df = itemsList.sort_values(by=['weightedSuccessLatency'])

    return df


def rankItems(itemsList: pd.DataFrame, weight_factor: int,
    expected_latency: float, max_fail_per_period: int,
    weight_multiplier=35) -> list:

    previousNodeLatency = 0
    raffle = []

    for ind, item in itemsList.iterrows():
        latencyDifference = 0
        benchmark = previousNodeLatency

        if 0 < previousNodeLatency and expected_latency < item.medianSuccessLatency:
            # 0 < prev lat < expected < median lat
            # prev < median -> reset benchmark
            if previousNodeLatency < expected_latency:
                benchmark = expected_latency

            # expected lat < median -> weighted - prev
            latencyDifference = item.weightedSuccessLatency - benchmark

        if latencyDifference:
            weight_factor -= np.round(latencyDifference * weight_multiplier)

            if (weight_factor <= 0):
                weight_factor = 0 if item.attempts >= max_fail_per_period else 1


        # TODO add failure conditions
        if item.successRate > 0.95:
            raffle.extend([ind] * int(weight_factor))
        elif item.successRate > 0:
            raffle.append(ind)
        else:
            if item.attempts < max_fail_per_period:
                raffle.append(ind)
            else:
                # TODO set failure in log
                pass

        previousNodeLatency = item.weightedSuccessLatency

    return raffle


def get_node(weight_factor=10, expected_latency=0.15, weight_multiplier=35) -> pd.DataFrame:
    max_failure_period = 3

    unsorted_data = unsortedList(filename="rawServiceLog.csv")
    sortedList = sortItems(itemsList=unsorted_data)
    rankedList = rankItems(
        itemsList=sortedList,
        weight_factor=weight_factor,
        expected_latency=expected_latency,
        weight_multiplier=weight_multiplier,
        max_fail_per_period=max_failure_period
        )

    # random pick of the list
    ind = np.floor(np.random.rand() * len(rankedList))
    node_ind = rankedList[int(ind)]

    return sortedList.loc[node_ind]


if __name__ == "__main__":
    res = get_node()
    print(res)