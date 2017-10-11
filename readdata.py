# coding=utf-8

import os


def read_local_data(localpath):
	print (os.listdir(localpath))
	pass


if __name__ == "__main__":
	localpath = "../data_lianlian"
	read_local_data(localpath)
