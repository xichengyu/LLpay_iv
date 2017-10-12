# coding=utf-8

import os
import numpy as np
import traceback


def read_local_data(localpath, default=-1.0):
    """
    read data from local place
    :param default: default value used to replace non_type value
    :param localpath: the path of data
    :return: the new numpy array in which None_type values are replaced with -1.0
    """
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
        res[:, idx][np.where(res[:, idx] == '\\N')[0]] = default
    print(res[0])
    return res


def delete_nonint_column(nparray):
    """
    delete columns whose type is string
    :param nparray:
    :return: the new numpy array
    """
    new_nparray = np.array([[]]*nparray.shape[0])
    for idx in range(nparray.shape[-1]):
        try:
            new_nparray = np.column_stack((new_nparray, res[:, idx].astype(float)))
        except ValueError:
            print(res[:, idx])
            traceback.print_exc()
            continue
    return new_nparray


if __name__ == "__main__":
    localpath = "../data_lianlian"
    res = read_local_data(localpath)
    new_nparray = delete_nonint_column(res)

    print(new_nparray.shape)
