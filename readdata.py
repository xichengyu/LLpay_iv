# coding=utf-8

import os


def read_local_data(localpath):
    files = os.listdir(localpath)
    for file in files:
        temp = open(localpath+"/%s" % file).readlines()
        print(type(temp))
        for line in temp:
            print(line)
    pass


if __name__ == "__main__":
    localpath = "../data_lianlian"
    read_local_data(localpath)

