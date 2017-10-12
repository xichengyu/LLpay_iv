# coding=utf-8

import os
import numpy as np


def read_local_data(localpath):
    files = os.listdir(localpath)
    res = []
    for file in files:
        temp = open(localpath + "/%s" % file).readlines()
        print(type(temp))
        print(temp[0].split(), len(temp[0].split()))
        for line in temp:
            res.append(line.split())
    print("total data: ", len(res))
    temp = np.array(res)

    res = np.copy(temp)
    for idx in range(res.shape[-1]):
        res[:, idx][np.where(res[:, idx] == '\\N')[0]] = -1.0

    print(res[0])

    pass


if __name__ == "__main__":
    localpath = "../data_lianlian"
    read_local_data(localpath)
