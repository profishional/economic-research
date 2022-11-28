import pandas as pd
import numpy as np

PATH = '/Users/df/other/pocket_files/pokt_tokenomics/data/'

# TODO get data from pypokt??
def unsortedList():
    # id, attempts, successStatuses, averageSuccessLatency
    df = pd.read_csv(PATH + 'rawServiceLog.csv')
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


def get_node(weightFactor=10):
    unsorted_data = unsortedList()
    sortedList = sortItems(itemsList=unsorted_data)
    ranked = rankItems(itemsList=sortedList, Fw=weightFactor)

    # create a raffle based on the weighting they got
    raffle = []
    for ind, node in ranked.iterrows():
        raffle.extend([node.id] * int(node['rank']))

    # random pick of the list
    ind = np.floor(np.random.rand() * len(raffle))
    node_id = raffle[int(ind)]

    return ranked.loc[ranked.id == node_id]


if __name__ == "__main__":
    res = get_node()
    print(int(res.id))