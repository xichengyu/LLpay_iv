# coding=utf-8

"""python 3.6"""

import sys
import numpy as np
# from inputs import fetch_from_hive
import read_data as rd
sys.path.append("information_value/")
from iv import WOE
from sklearn.externals import joblib
from read_cnf import get_conf_info

conf_info = get_conf_info()

if 0:
    localpath = "../data_lianlian"
    res = rd.read_local_data(localpath)
else:
    localpath = "%s" % conf_info["raw_data_dump_path"]
    res = rd.load_local_data(localpath)
joblib.dump(res, "conf/raw_data.dt")
new_nparray = rd.delete_str_column(res)
joblib.dump(new_nparray, "conf/float_data.dt")

X = new_nparray
joblib.dump(X, "conf/input_data.dt")

rd.print_info(X.shape)

cal_woe = WOE()
WOE.WOE_N = int(conf_info["iv_n"])
X = cal_woe.feature_discretion(X)

print(X)

