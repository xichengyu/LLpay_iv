# coding=utf-8

"""python 2.7"""

import sys
import numpy as np
sys.path.append("../information_value/src")

from inputs import fetch_from_hive
import information_value


test_sql = "select * from dbmodel.data_lianlian_idno_pro limit 10"


X = np.array(fetch_from_hive(test_sql))

woe = information_value.WOE()

print (X)
