# coding=utf-8

"""python 3.6"""

# import sys
import numpy as np
from inputs import fetch_from_hive
import information_value as cal_iv


# test_sql = 'select count(*) from dbmodel.data_lianlian_idno_pro A inner join dbmodel.loan_data B ' \
#            'on A.id_no_hash = B.id_no_hash and A.dt_apply = B.dt_apply where B.status in ("已逾期", "还款完成")'

# test_sql = 'select * from dbmodel.data_lianlian_idno_pro A inner join dbmodel.loan_data B ' \
#            'on A.id_no_hash = B.id_no_hash and A.dt_apply = B.dt_apply where B.status in ("已逾期", "还款完成") limit 10'

test_sql = 'select * from dbmodel.data_lianlian_idno_pro limit 100'

X = np.array(fetch_from_hive(test_sql))

print (X)

y = [1]*10+[0]*90

print (y)

woe = cal_iv.WOE()

res_woe, res_iv = woe.woe(X, y, 1)

print (res_woe)
print (res_iv)