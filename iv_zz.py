# coding=utf-8

"""python 2.7"""

import sys
import numpy as np
sys.path.append("/information_value/src")

from inputs import fetch_from_hive
from information_value import WOE
import information_value as cal_iv


test_sql = "select * from dbmodel.data_lianlian_idno_pro limit 10"


X = np.array(fetch_from_hive(test_sql))

print (X)

woe = cal_iv.WOE()
