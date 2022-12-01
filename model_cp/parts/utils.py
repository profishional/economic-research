import pandas as pd
import numpy as np

# relative path of where all the data should be
PATH = '../../data/'

def unsortedList(filename="rawServiceLog.csv") -> pd.DataFrame:
    # id, attempts, successStatuses, averageSuccessLatency
    df = pd.read_csv(PATH + filename)
    df['successRate'] = np.round(df['successStatus']/ df['attempts'],5)

    return df


def sortItems(itemsList: pd.DataFrame) -> pd.DataFrame:
    # sort by success rate and tie break with ASL
    df = itemsList.sort_values(by=['successRate', 'averageSuccessLatency'])

    return df


def rankItems(itemsList: pd.DataFrame, weightFactor: int, maxFailurePerPeriod: int) -> list:
    # TODO time consideration
    # 15 failures per 15 minutes allowed on apps (all 5 nodes failed 3 times)??
    # 3 failures per hour

    raffle = []

    for ind, item in itemsList.iterrows():
        if item.successRate > 0.95:
            raffle.extend([ind] * weightFactor)
            weightFactor -= 2

        elif item.successRate > 0.85:
            raffle.extend([ind] * weightFactor)
            weightFactor = weightFactor - 3 if weightFactor <= 0 else 1

        elif item.successRate > 0:
            raffle.extend([ind])

        elif item.successRate == 0:
            if item.attempts < maxFailurePerPeriod:
                raffle.extend([ind])

    return raffle


def get_node(weightFactor=10, maxFailurePerPeriod=3) -> pd.DataFrame:
    unsorted_data = unsortedList(filename="rawServiceLog.csv")
    sortedList = sortItems(itemsList=unsorted_data)
    rankedList = rankItems(
        itemsList=sortedList,
        weightFactor=weightFactor,
        maxFailurePerPeriod=maxFailurePerPeriod
        )

    # random pick of the list
    ind = np.floor(np.random.rand() * len(rankedList))
    node_id = rankedList[int(ind)]

    return sortedList.loc[sortedList.id == node_id]


if __name__ == "__main__":
    res = get_node()
    print(res)