# coding=utf-8

import numpy as np
from sklearn.externals import joblib

iv = joblib.load("iv.nparray")
columns = [x.strip() for x in open("../new_column_name.txt").readlines()]
fout = open("csv/zz_iv_test.csv", "w")
fout.write(",".join(columns)+"\n")
fout.write(",".join([str(x) for x in list(iv)]))
fout.close()
