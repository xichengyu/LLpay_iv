# coding=utf-8

import os


def read_local_data(localpath):
    files = os.listdir(localpath)
    for file in files:
        temp = open(localpath+"/%s" % file).readlines()
        print(type(temp))
        # for line in temp:
            # print(line)
        print(temp[0].split())
    pass


if __name__ == "__main__":
    localpath = "../data_lianlian"
    read_local_data(localpath)

