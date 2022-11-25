import pandas as pd
import numpy as np


# TODO get data from pypokt??
def unsortedList(path):
    # id, attempts, successStatuses, averageSuccessLatency
    df = pd.read_csv(path)
    df['successRate'] = np.round(df['successStatus']/ df['attempts'],5)

    return df

# TODO sort by higher success rate, then lowest latency
def sortItems(itemsList):
    # key = success rate
    df = itemsList.sort_values(by=['successRate'])

    # tie breaker = avg success
    # df = itemsList.sort_values(by=['successRate', 'avarageSuccessLatency'])

    return df


# TODO weighted rank
def rankItems(itemsList, Fw):
    # 15 failures per 15 minutes allowed on apps (all 5 nodes failed 3 times)??
    # 3 failures per hour
    # >95% - 10
    itemsList['rank'] = np.where(itemsList['successRate'] > .95, Fw, 1)

    # >85% - 8
    # >0% - 5 or 1
    # else 1
    # remove if fail > 3

    return itemsList


def get_node(data_file='../../data/rawServiceLog.csv'):
    data = unsortedList(data_file)
    sortedList = sortItems(itemsList=data)
    ranked = rankItems(itemsList=sortedList, Fw=10)
    ind = np.floor(np.random.rand() * len(ranked))

    return ranked.loc[ind]


if __name__ == "__main__":
    res = get_node()
    print(res)