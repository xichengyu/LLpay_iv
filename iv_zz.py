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
from sklearn.preprocessing import Imputer
from pandas import DataFrame

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

y = new_nparray[:, int(conf_info["y_idx"])]
X = np.delete(new_nparray, int(conf_info["y_idx"]), axis=1)
joblib.dump(X, "conf/input_data.dt")

impute = Imputer(X, strategy="median")
X = impute.fit_transform(X)
rd.print_info(DataFrame(X))

rd.print_info(X.shape)
rd.print_info(y.sum(), np.count_nonzero(y))

cal_woe = WOE()
WOE.WOE_N = int(conf_info["iv_n"])
res_woe, res_iv = cal_woe.woe(X, y)

rd.print_info(res_woe, res_woe.shape)
joblib.dump(res_woe, "conf/woe.nparray")
rd.print_info(res_iv, res_iv.shape)
joblib.dump(res_iv, "conf/iv.nparray")

