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
print("raw_data: ", res[0, :])

idno = res[:, 0]
idno_dt = np.column_stack((idno, res[:, 1]))
print(idno_dt.shape)

new_nparray = rd.delete_str_column(res)
joblib.dump(new_nparray, "conf/float_data.dt")
print("delete_str: ", new_nparray[0, :])


tmp_idno_dt = []
tmp_new_nparray = []

for idx in range(new_nparray.shape[0]):
    print(sum(new_nparray[idx, :]),  -1*new_nparray.shape[-1])
    if sum(new_nparray[idx, :]) == -1*new_nparray.shape[-1]:
        continue
    tmp_idno_dt.append(idno_dt[idx, :])
    tmp_new_nparray.append(new_nparray[idx, :])

idno_dt = np.array(tmp_idno_dt)
new_nparray = np.array(tmp_new_nparray)

X = new_nparray
joblib.dump(X, "conf/input_data.dt")

rd.print_info(X.shape)

cal_woe = WOE()
WOE.WOE_N = int(conf_info["iv_n"])
X = cal_woe.feature_discretion(X)

X = np.column_stack((idno_dt, X))
print("X: ", X[0, :])

joblib.dump(X, "conf/zhangzhong_result.dt")

fout = open("conf/result.csv", "w")
for idx in range(X.shape[0]):
    x_list = list(X[idx, :].astype(str))
    fout.write(",".join(x_list)+"\n")

fout.close()
print(X)

