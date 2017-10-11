# coding=utf-8

"""python 2.7"""

import sys
import numpy as np
sys.path.append("information_value/src")


from inputs import fetch_from_hive
import information_value as cal_iv


# test_sql = 'select count(*) from dbmodel.data_lianlian_idno_pro A inner join dbmodel.loan_data B ' \
#            'on A.id_no_hash = B.id_no_hash and A.dt_apply = B.dt_apply where B.status in ("已逾期", "还款完成")'

test_sql = 'select * from dbmodel.data_lianlian_idno_pro A inner join dbmodel.loan_data B ' \
           'on A.id_no_hash = B.id_no_hash and A.dt_apply = B.dt_apply where B.status in ("已逾期", "还款完成") limit 10'


X = np.array(fetch_from_hive(test_sql))

print (X)

woe = cal_iv.WOE()
