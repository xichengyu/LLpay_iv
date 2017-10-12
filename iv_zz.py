# coding=utf-8

"""python 3.6"""

import sys
import numpy as np
# from inputs import fetch_from_hive
import readdata as rd
sys.path.append("information_value/")
from iv import WOE


localpath = "../data_lianlian"

res = rd.read_local_data(localpath)
new_nparray = rd.delete_str_column(res)

y = new_nparray[:, -1]

X = np.delete(new_nparray, -1, axis=1)

print(X.shape)

print(y)

cal_woe = WOE()

# res_woe, res_iv = woe.woe(X, y, 1)

# print(res_woe)
# print(res_iv)
