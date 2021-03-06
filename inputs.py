# coding=utf-8

"""python 3.6"""

from __future__ import absolute_import, division, print_function

# import itertools
import logging
# import os
# import random
# import re
# import functools
# from string import Template

import numpy as np
# import pandas as pd
from sklearn.externals import joblib
from read_cnf import get_conf_info

logging.basicConfig(level=logging.ERROR)
logging.getLogger('../hivelog/pyhive.log').setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


features_104 = ['sex','age','signcnttrdxd','signcnttrd_7dxd','signcnttrd_30dxd','signcnttrd_90dxd','signcnttrd_180dxd','sign_first_daysxd','sign_last_daysxd','signcnttrd_fq','signcnttrd_90d_fq','signcnttrd_180d_fq','sign_first_days_fq','sign_last_days_fq','paycnttrdxd','paycnttrd_30dxd','payminamtxd','pay_sumamtxd','paymaxamtxd','paycntamtxd','paycntamt_30dxd','paycntamt_90dxd','paycntamt_180dxd','pay_sumamt_7dxd','pay_sumamt_30dxd','pay_sumamt_90dxd','pay_sumamt_180dxd','pay_first_daysxd','pay_last_daysxd','paycntamtxd_nediv10','paycntamtxd_nediv100','paycntamtxd_bt200_nediv100','paycntamtxd_nediv1','pay_last_daysxd_nediv1','pay_last_daysxd_lt200','paycntamt_suda','paycntamt_yuntu','payovdmaxxd_lt500_xudai','payovdminxd_lt500_xudai','payovdcntxd_lt500_xudai','payovdamtxd_lt500_xudai','payovd_avgxd_lt500_xudai','paycntamtxd_lt500_xudai','paycntamtxd_nediv10_30d','paycntamtxd_nediv100_30d','payovdmaxxd_lt500_xudai_30d','payovdcntxd_lt500_xudai_7d','payovdamtxd_lt500_xudai_7d','payovd_avgxd_lt500_xudai_7d','paycntamtxd_nediv10_60d','paycntamtxd_nediv100_60d','paycntamtxd_bt200_nediv100_60d','paycntamtxd_nediv1_60d','paycntamt_suda_60d','paycntamt_yuntu_60d','payovdmaxxd_lt500_xudai_60d','payovdminxd_lt500_xudai_60d','payovdcntxd_lt500_xudai_60d','payovdamtxd_lt500_xudai_60d','payovd_avgxd_lt500_xudai_60d','paycntamtxd_lt500_xudai_60d','paycntamtxd_nediv10_90d','paycntamtxd_nediv100_90d','paycntamtxd_bt200_nediv100_90d','paycntamt_suda_90d','payovdmaxxd_lt500_xudai_90d','payovdminxd_lt500_xudai_90d','payovdcntxd_lt500_xudai_90d','payovdamtxd_lt500_xudai_90d','payovd_avgxd_lt500_xudai_90d','paycntamtxd_lt500_xudai_90d','paycntamtxd_gt500_nxudai_90d','payminamt_fq','pay_sumamt_fq','paymaxamt_fq','paycntamt_fq','paycntamt_180d_fq','pay_sumamt_30d_fq','pay_sumamt_90d_fq','pay_sumamt_180d_fq','p2pmin_amt','p2p_sum_amt','p2pmax_amt','p2pcnt_amt','pay_first_days_fq','pay_last_days_fq','paytrdmin_amt','paytrdmaxcnt_60d','passcnttrd_7dxd','passminamtxd','pass_sumamtxd','passmaxamtxd','passcntamtxd','pass_sumamt_7dxd','pass_sumamt_30dxd','pass_sumamt_90dxd','pass_sumamt_180dxd','passcntamt_7dxd','passcntamt_30dxd','passcntamt_90dxd','passcntamt_180dxd','pass_first_daysxd','pass_last_daysxd','pass_last_days_fq']
features_fenqi = ['sex','age','signcnttrdxd','signcnttrd_7dxd','signcnttrd_3dxd','signcnttrd_30dxd','signcnttrd_90dxd','signcnttrd_180dxd','sign_first_daysxd','sign_last_daysxd','signcnttrd_fq','signcnttrd_7d_fq','signcnttrd_3d_fq','signcnttrd_30d_fq','signcnttrd_90d_fq','signcnttrd_180d_fq','sign_first_days_fq','sign_last_days_fq','paycnttrdxd','paycnttrd_7dxd','paycnttrd_3dxd','paycnttrd_30dxd','paycnttrd_90dxd','paycnttrd_180dxd','payminamtxd','pay_sumamtxd','paymaxamtxd','paycntamtxd','paycntamt_7dxd','paycntamt_3dxd','paycntamt_30dxd','paycntamt_90dxd','paycntamt_180dxd','pay_sumamt_7dxd','pay_sumamt_3dxd','pay_sumamt_30dxd','pay_sumamt_90dxd','pay_sumamt_180dxd','pay_first_daysxd','pay_last_daysxd','paycntamtxd_nediv10','paycntamtxd_nediv100','paycntamtxd_bt200_nediv100','paycntamtxd_lt200_ediv10','paycntamtxd_nediv1','pay_last_daysxd_nediv1','pay_last_daysxd_lt200','paycntamt_suda','paycntamt_beidufen','paycntamt_huawuque','paycntamt_yuntu','payovdmaxxd_lt500_xudai','payovdminxd_lt500_xudai','payovdcntxd_lt500_xudai','payovdamtxd_lt500_xudai','payovd_avgxd_lt500_xudai','paycntamtxd_lt500_xudai','paycntamtxd_gt500_nxudai','paycntamtxd_nediv10_30d','paycntamtxd_nediv100_30d','paycntamtxd_bt200_nediv100_30d','paycntamtxd_lt200_ediv10_30d','paycntamtxd_nediv1_30d','paycntamt_suda_30d','paycntamt_beidufen_30d','paycntamt_huawuque_30d','paycntamt_yuntu_30d','payovdmaxxd_lt500_xudai_30d','payovdminxd_lt500_xudai_30d','payovdcntxd_lt500_xudai_30d','payovdamtxd_lt500_xudai_30d','payovd_avgxd_lt500_xudai_30d','paycntamtxd_lt500_xudai_30d','paycntamtxd_gt500_nxudai_30d','paycntamtxd_nediv10_7d','paycntamtxd_nediv100_7d','paycntamtxd_bt200_nediv100_7d','paycntamtxd_lt200_ediv10_7d','paycntamtxd_nediv1_7d','paycntamt_suda_7d','paycntamt_beidufen_7d','paycntamt_huawuque_7d','paycntamt_yuntu_7d','payovdmaxxd_lt500_xudai_7d','payovdminxd_lt500_xudai_7d','payovdcntxd_lt500_xudai_7d','payovdamtxd_lt500_xudai_7d','payovd_avgxd_lt500_xudai_7d','paycntamtxd_lt500_xudai_7d','paycntamtxd_gt500_nxudai_7d','paycntamtxd_nediv10_3d','paycntamtxd_nediv100_3d','paycntamtxd_bt200_nediv100_3d','paycntamtxd_lt200_ediv10_3d','paycntamtxd_nediv1_3d','paycntamt_suda_3d','paycntamt_beidufen_3d','paycntamt_huawuque_3d','paycntamt_yuntu_3d','payovdmaxxd_lt500_xudai_3d','payovdminxd_lt500_xudai_3d','payovdcntxd_lt500_xudai_3d','payovdamtxd_lt500_xudai_3d','payovd_avgxd_lt500_xudai_3d','paycntamtxd_lt500_xudai_3d','paycntamtxd_gt500_nxudai_3d','paycntamtxd_nediv10_60d','paycntamtxd_nediv100_60d','paycntamtxd_bt200_nediv100_60d','paycntamtxd_lt200_ediv10_60d','paycntamtxd_nediv1_60d','paycntamt_suda_60d','paycntamt_beidufen_60d','paycntamt_huawuque_60d','paycntamt_yuntu_60d','payovdmaxxd_lt500_xudai_60d','payovdminxd_lt500_xudai_60d','payovdcntxd_lt500_xudai_60d','payovdamtxd_lt500_xudai_60d','payovd_avgxd_lt500_xudai_60d','paycntamtxd_lt500_xudai_60d','paycntamtxd_gt500_nxudai_60d','paycntamtxd_nediv10_90d','paycntamtxd_nediv100_90d','paycntamtxd_bt200_nediv100_90d','paycntamtxd_lt200_ediv10_90d','paycntamtxd_nediv1_90d','paycntamt_suda_90d','paycntamt_beidufen_90d','paycntamt_huawuque_90d','paycntamt_yuntu_90d','payovdmaxxd_lt500_xudai_90d','payovdminxd_lt500_xudai_90d','payovdcntxd_lt500_xudai_90d','payovdamtxd_lt500_xudai_90d','payovd_avgxd_lt500_xudai_90d','paycntamtxd_lt500_xudai_90d','paycntamtxd_gt500_nxudai_90d','paycnttrd_fq','paycnttrd_3d_fq','paycnttrd_7d_fq','paycnttrd_30d_fq','paycnttrd_90d_fq','paycnttrd_180d_fq','payminamt_fq','pay_sumamt_fq','paymaxamt_fq','paycntamt_fq','paycntamt_3d_fq','paycntamt_7d_fq','paycntamt_30d_fq','paycntamt_90d_fq','paycntamt_180d_fq','pay_sumamt_3d_fq','pay_sumamt_7d_fq','pay_sumamt_30d_fq','pay_sumamt_90d_fq','pay_sumamt_180d_fq','p2pmin_amt','p2p_sum_amt','p2pmax_amt','p2pcnt_amt','pay_first_days_fq','pay_last_days_fq','paytrdcnttrd_pay500_times2','paytrdmin_amt','paytrdmax_amt','paytrdmin_avg_amt','paytrdmax_avg_amt','paytrdmax_count','paytrdmaxcnt_pay500','paytrdcnttrd_pay500_times2_30d','paytrdminamt_30d','paytrdmaxamt_30d','paytrdmin_avgamt_30d','paytrdmax_avgamt_30d','paytrdmaxcnt_30d','paytrdmaxcnt_pay500_30d','paytrdcnttrd_pay500_times2_7d','paytrdminamt_7d','paytrdmaxamt_7d','paytrdmin_avgamt_7d','paytrdmax_avgamt_7d','paytrdmaxcnt_7d','paytrdmaxcnt_pay500_7d','paytrdcnttrd_pay500_times2_3d','paytrdminamt_3d','paytrdmaxamt_3d','paytrdmin_avgamt_3d','paytrdmax_avgamt_3d','paytrdmaxcnt_3d','paytrdmaxcnt_pay500_3d','paytrdcnttrd_pay500_times2_60d','paytrdminamt_60d','paytrdmaxamt_60d','paytrdmin_avgamt_60d','paytrdmax_avgamt_60d','paytrdmaxcnt_60d','paytrdmaxcnt_pay500_60d','paytrdcnttrd_pay500_times2_90d','paytrdminamt_90d','paytrdmaxamt_90d','paytrdmin_avgamt_90d','paytrdmax_avgamt_90d','paytrdmaxcnt_90d','paytrdmaxcnt_pay500_90d','passcnttrdxd','passcnttrd_3dxd','passcnttrd_7dxd','passcnttrd_30dxd','passcnttrd_90dxd','passcnttrd_180dxd','passminamtxd','pass_sumamtxd','passmaxamtxd','passcntamtxd','pass_sumamt_3dxd','pass_sumamt_7dxd','pass_sumamt_30dxd','pass_sumamt_90dxd','pass_sumamt_180dxd','passcntamt_3dxd','passcntamt_7dxd','passcntamt_30dxd','passcntamt_90dxd','passcntamt_180dxd','pass_first_daysxd','pass_last_daysxd','passcnttrd_fq','passcnttrd_3d_fq','passcnttrd_7d_fq','passcnttrd_30d_fq','passcnttrd_90d_fq','passcnttrd_180d_fq','passminamt_fq','pass_sumamt_fq','passmaxamt_fq','passcntamt_fq','pass_sumamt_3d_fq','pass_sumamt_7d_fq','pass_sumamt_30d_fq','pass_sumamt_90d_fq','pass_sumamt_180d_fq','passcntamt_3d_fq','passcntamt_7d_fq','passcntamt_30d_fq','passcntamt_90d_fq','passcntamt_180d_fq','pass_first_days_fq','pass_last_days_fq','depay_cnt_7_error_90d','depay_maxlagtime_30d','depay_cnt_7_error_hist','depay_cnt_9_error_hist','depay_radio_plandebt_hist','depay_cntlagtime_30d','depay_cntpartno_30d','depaycnt_over7d_180d','depay_minus_plandebt__hist','depay_cnt_9_error_7d','depaycnt_over_180d','depay_cntpartno_90d','depay_sumsche_90d','depay_cnt_5_error_30d','depay_cntontime_s_7d','depay_cnt_9_error_30d','depay_cnt_times_lowsch_hist','depay_cnt_3_error_hist','depay_sumrepay_30d','depay_sumact_90d','depay_cnt_8_error_30d','depaycnt_over30d_90d','depay_cntontime_30d','depay_avgplan_hist','depay_cntplanno_7d','depay_cnt_12_error_7d','depay_cntplanno_hist','depay_cntontime_hist','depay_cnt_17_error_hist','depaycnt_90d','depay_sumrepay_7d','depay_cnt_9_error_90d','depay_cnt_14_error_30d','depay_cntpartno_hist','depay_cnt_4_error_90d','depay_maxamt_7d','depay_sumplan_30d','depay_cnt_16_error_hist','depay_cnt_6_error_90d','depay_cntontime_s_30d','depay_cnt_5_error_90d','depay_cnt_2_error_90d','depay_cnt_1_error_7d','depaycnt_over15d_90d','depay_maxamt_90d','depay_avgplan_30d','depay_cntfail_hist','depay_cnt_11_error_hist','depay_minus_plandebt_90d','depay_sumlagtime_90d','depaycnt_over3d_360d','depay_cntfail_90d','depaycnt_over7d_360d','depay_cnt_17_error_7d','depay_sumlagtime_hist','depay_cnt_3_error_90d','depay_maxlagtime_90d','depaycnt_over3d_30d','depay_cnt_6_error_hist','depay_radio_plandebt_90d','depay_cnt_7_error_7d','depay_sumact_hist','depaycnt_over_60d','depaycnt_over15d_180d','depay_cnt_3_error_7d','depay_cnt_14_error_hist','depay_maxamt_hist','depay_decntplanno_30d','depaycnt_360d','depay_cnt_5_error_7d','depay_cnt_2_error_30d','depaycnt_60d','depay_cnt_4_error_30d','depay_cnt_11_error_7d','depay_cnt_times_lowsch_90d','depay_cnt_times_lowsch_7d','depaycnt_over_30d','depay_cnt_12_error_hist','depay_sumfir_90d','depay_cntlagtime_hist','depay_cnt_1_error_30d','depay_sumplan_90d','depay_sumsche_30d','depaycnt_over7d_30d','depay_avgamt_90d','depay_cntfail_30d','depay_cnt_10_error_30d','depay_sumfir_hist','depay_maxlagtime_hist','depay_cnt_2_error_hist','depay_sumplan_7d','depay_cntplanno_30d','depay_cnt_6_error_30d','depay_cnt_3_error_30d','depay_minus_plandebt_30d','depay_cnt_12_error_30d','depay_cnt_1_error_90d','depaycnt_over3d_180d','depaycnt_over7d_90d','depay_sumfir_7d','depay_maxlagtime_7d','depay_cntpartno_7d','depay_decntplanno_90d','depaycnt_over3d_90d','depay_sumlagtime_7d','depay_cnt_13_error_7d','depay_sumlagtime_30d','depaycnt_over3d_60d','depay_cnt_5_error_hist','depaycnt_over7d_60d','depaycnt_over15d_30d','depay_cnt_11_error_30d','depay_cnt_13_error_90d','depay_cnt_16_error_7d','depay_cnt_13_error_hist','depay_sumact_30d','depay_cnt_7_error_30d','depaycnt_over15d_360d','depaycnt_over15d_60d','depay_sumrepay_hist','depay_sumamt_90d','depay_cntontime_s_hist','depay_cntontime_s_90d','depaycnt_30d','depaycnt_over30d_30d','depay_cntplanno_60d','depay_cnt_times_lowsch_30d','depay_cnt_8_error_90d','depay_sumsche_hist','depay_cntfail_7d','depay_cnt_14_error_90d','depay_cnt_10_error_hist','depay_cnt_16_error_30d','depay_maxamt_30d','depaycnt_over_90d','depay_cnt_11_error_90d','depaycnt_180d','depay_avgamt_30d','depay_cnt_8_error_7d','depay_cntlagtime_90d','depay_decntplanno_7d','depay_sumamt_7d','depay_avgplan_90d','depay_radio_plandebt_30d','depay_cnt_16_error_90d','depay_cntontime_90d','depay_minus_plandebt_7d','depaycnt_over30d_180d','depay_sumamt_30d','depay_cnt_10_error_90d','depay_sumrepay_90d','depay_radio_plandebt_7d','depay_cnt_1_error_hist','depay_sumsche_7d','depay_decntplanno_hist','depaycnt_over30d_360d','depay_sumamt_hist','depay_avgamt_hist','depay_cntlagtime_7d','depay_cnt_4_error_7d','depaycnt_over_360d','depay_cnt_14_error_7d','depay_avgplan_7d','depay_cnt_17_error_90d','depay_cnt_2_error_7d','depay_cnt_4_error_hist','depaycnt_over30d_60d','depay_sumact_7d','depay_cnt_10_error_7d','depay_cnt_12_error_90d','depay_cnt_13_error_30d','depay_sumfir_30d','depay_cnt_6_error_7d','depay_sumplan_hist','depay_cntontime_7d','depay_cnt_17_error_30d','depay_cnt_8_error_hist','depay_avgamt_7d']
features_250 = ['sex','age','signcnttrdxd','signcnttrd_7dxd','signcnttrd_3dxd','signcnttrd_30dxd','signcnttrd_90dxd','signcnttrd_180dxd','sign_first_daysxd','sign_last_daysxd','signcnttrd_fq','signcnttrd_7d_fq','signcnttrd_3d_fq','signcnttrd_30d_fq','signcnttrd_90d_fq','signcnttrd_180d_fq','sign_first_days_fq','sign_last_days_fq','paycnttrdxd','paycnttrd_7dxd','paycnttrd_3dxd','paycnttrd_30dxd','paycnttrd_90dxd','paycnttrd_180dxd','payminamtxd','pay_sumamtxd','paymaxamtxd','paycntamtxd','paycntamt_7dxd','paycntamt_3dxd','paycntamt_30dxd','paycntamt_90dxd','paycntamt_180dxd','pay_sumamt_7dxd','pay_sumamt_3dxd','pay_sumamt_30dxd','pay_sumamt_90dxd','pay_sumamt_180dxd','pay_first_daysxd','pay_last_daysxd','paycntamtxd_nediv10','paycntamtxd_nediv100','paycntamtxd_bt200_nediv100','paycntamtxd_lt200_ediv10','paycntamtxd_nediv1','pay_last_daysxd_nediv1','pay_last_daysxd_lt200','paycntamt_suda','paycntamt_beidufen','paycntamt_huawuque','paycntamt_yuntu','payovdmaxxd_lt500_xudai','payovdminxd_lt500_xudai','payovdcntxd_lt500_xudai','payovdamtxd_lt500_xudai','payovd_avgxd_lt500_xudai','paycntamtxd_lt500_xudai','paycntamtxd_gt500_nxudai','paycntamtxd_nediv10_30d','paycntamtxd_nediv100_30d','paycntamtxd_bt200_nediv100_30d','paycntamtxd_lt200_ediv10_30d','paycntamtxd_nediv1_30d','paycntamt_suda_30d','paycntamt_beidufen_30d','paycntamt_huawuque_30d','paycntamt_yuntu_30d','payovdmaxxd_lt500_xudai_30d','payovdminxd_lt500_xudai_30d','payovdcntxd_lt500_xudai_30d','payovdamtxd_lt500_xudai_30d','payovd_avgxd_lt500_xudai_30d','paycntamtxd_lt500_xudai_30d','paycntamtxd_gt500_nxudai_30d','paycntamtxd_nediv10_7d','paycntamtxd_nediv100_7d','paycntamtxd_bt200_nediv100_7d','paycntamtxd_lt200_ediv10_7d','paycntamtxd_nediv1_7d','paycntamt_suda_7d','paycntamt_beidufen_7d','paycntamt_huawuque_7d','paycntamt_yuntu_7d','payovdmaxxd_lt500_xudai_7d','payovdminxd_lt500_xudai_7d','payovdcntxd_lt500_xudai_7d','payovdamtxd_lt500_xudai_7d','payovd_avgxd_lt500_xudai_7d','paycntamtxd_lt500_xudai_7d','paycntamtxd_gt500_nxudai_7d','paycntamtxd_nediv10_3d','paycntamtxd_nediv100_3d','paycntamtxd_bt200_nediv100_3d','paycntamtxd_lt200_ediv10_3d','paycntamtxd_nediv1_3d','paycntamt_suda_3d','paycntamt_beidufen_3d','paycntamt_huawuque_3d','paycntamt_yuntu_3d','payovdmaxxd_lt500_xudai_3d','payovdminxd_lt500_xudai_3d','payovdcntxd_lt500_xudai_3d','payovdamtxd_lt500_xudai_3d','payovd_avgxd_lt500_xudai_3d','paycntamtxd_lt500_xudai_3d','paycntamtxd_gt500_nxudai_3d','paycntamtxd_nediv10_60d','paycntamtxd_nediv100_60d','paycntamtxd_bt200_nediv100_60d','paycntamtxd_lt200_ediv10_60d','paycntamtxd_nediv1_60d','paycntamt_suda_60d','paycntamt_beidufen_60d','paycntamt_huawuque_60d','paycntamt_yuntu_60d','payovdmaxxd_lt500_xudai_60d','payovdminxd_lt500_xudai_60d','payovdcntxd_lt500_xudai_60d','payovdamtxd_lt500_xudai_60d','payovd_avgxd_lt500_xudai_60d','paycntamtxd_lt500_xudai_60d','paycntamtxd_gt500_nxudai_60d','paycntamtxd_nediv10_90d','paycntamtxd_nediv100_90d','paycntamtxd_bt200_nediv100_90d','paycntamtxd_lt200_ediv10_90d','paycntamtxd_nediv1_90d','paycntamt_suda_90d','paycntamt_beidufen_90d','paycntamt_huawuque_90d','paycntamt_yuntu_90d','payovdmaxxd_lt500_xudai_90d','payovdminxd_lt500_xudai_90d','payovdcntxd_lt500_xudai_90d','payovdamtxd_lt500_xudai_90d','payovd_avgxd_lt500_xudai_90d','paycntamtxd_lt500_xudai_90d','paycntamtxd_gt500_nxudai_90d','paycnttrd_fq','paycnttrd_3d_fq','paycnttrd_7d_fq','paycnttrd_30d_fq','paycnttrd_90d_fq','paycnttrd_180d_fq','payminamt_fq','pay_sumamt_fq','paymaxamt_fq','paycntamt_fq','paycntamt_3d_fq','paycntamt_7d_fq','paycntamt_30d_fq','paycntamt_90d_fq','paycntamt_180d_fq','pay_sumamt_3d_fq','pay_sumamt_7d_fq','pay_sumamt_30d_fq','pay_sumamt_90d_fq','pay_sumamt_180d_fq','p2pmin_amt','p2p_sum_amt','p2pmax_amt','p2pcnt_amt','pay_first_days_fq','pay_last_days_fq','paytrdcnttrd_pay500_times2','paytrdmin_amt','paytrdmax_amt','paytrdmin_avg_amt','paytrdmax_avg_amt','paytrdmax_count','paytrdmaxcnt_pay500','paytrdcnttrd_pay500_times2_30d','paytrdminamt_30d','paytrdmaxamt_30d','paytrdmin_avgamt_30d','paytrdmax_avgamt_30d','paytrdmaxcnt_30d','paytrdmaxcnt_pay500_30d','paytrdcnttrd_pay500_times2_7d','paytrdminamt_7d','paytrdmaxamt_7d','paytrdmin_avgamt_7d','paytrdmax_avgamt_7d','paytrdmaxcnt_7d','paytrdmaxcnt_pay500_7d','paytrdcnttrd_pay500_times2_3d','paytrdminamt_3d','paytrdmaxamt_3d','paytrdmin_avgamt_3d','paytrdmax_avgamt_3d','paytrdmaxcnt_3d','paytrdmaxcnt_pay500_3d','paytrdcnttrd_pay500_times2_60d','paytrdminamt_60d','paytrdmaxamt_60d','paytrdmin_avgamt_60d','paytrdmax_avgamt_60d','paytrdmaxcnt_60d','paytrdmaxcnt_pay500_60d','paytrdcnttrd_pay500_times2_90d','paytrdminamt_90d','paytrdmaxamt_90d','paytrdmin_avgamt_90d','paytrdmax_avgamt_90d','paytrdmaxcnt_90d','paytrdmaxcnt_pay500_90d','passcnttrdxd','passcnttrd_3dxd','passcnttrd_7dxd','passcnttrd_30dxd','passcnttrd_90dxd','passcnttrd_180dxd','passminamtxd','pass_sumamtxd','passmaxamtxd','passcntamtxd','pass_sumamt_3dxd','pass_sumamt_7dxd','pass_sumamt_30dxd','pass_sumamt_90dxd','pass_sumamt_180dxd','passcntamt_3dxd','passcntamt_7dxd','passcntamt_30dxd','passcntamt_90dxd','passcntamt_180dxd','pass_first_daysxd','pass_last_daysxd','passcnttrd_fq','passcnttrd_3d_fq','passcnttrd_7d_fq','passcnttrd_30d_fq','passcnttrd_90d_fq','passcnttrd_180d_fq','passminamt_fq','pass_sumamt_fq','passmaxamt_fq','passcntamt_fq','pass_sumamt_3d_fq','pass_sumamt_7d_fq','pass_sumamt_30d_fq','pass_sumamt_90d_fq','pass_sumamt_180d_fq','passcntamt_3d_fq','passcntamt_7d_fq','passcntamt_30d_fq','passcntamt_90d_fq','passcntamt_180d_fq','pass_first_days_fq','pass_last_days_fq']

'''
sql_plain = Template(
select
    id_no_hash,
    dt_apply,
    label,
    $columns
from
    (select
        trader_no,
        id_no_hash as id,
        dt_apply as dt,
        case when overdue_days > 20 then '1' else case when status = '还款完成' and overdue_days < 20 then '0' else null end end as label
    from dbmodel.loan_data
    where
        trader_no in ('001', '002', '003', '004', '005', '007') 
        and status in ('还款完成', '已逾期'))u,
    dbmodel.data_lianlian_idno_dl l
where
    u.id = l.id_no_hash
    and u.dt = l.dt_apply
    and label in ('0', '1')
    and (l.signcnttrdxd > 0 and SIGNCNTTRD_FQ > 0) 
)
'''
'''
sql_fenqi = Template(
select
    u.id_no_hash as id_no_hash,
    unix_timestamp(u.dt_apply) as dt_apply,
    label,
    $columns
from
    (select
        trader_no,
        id_no_hash,
        dt_apply,
        case when overdue_days > 20 then '1' else case when status = '还款完成' and overdue_days < 20 then '0' else null end end as label
    from dbmodel.loan_data
    where
        trader_no in ('001', '002', '003', '004', '005', '007', '008')
        and status in ('还款完成', '已逾期'))u,
    dbmodel.data_repay_idno_dl l,
    dbmodel.data_lianlian_idno_dl y
where
    u.id_no_hash = l.id_no_hash and l.id_no_hash = y.id_no_hash
    and u.dt_apply = l.dt_apply and l.dt_apply = y.dt_apply
    and label in ('0', '1')
    and (y.signcnttrdxd > 0 or y.SIGNCNTTRD_FQ > 0) 
)
'''


def fetch_from_hive(sql):
    if not isinstance(sql, str):
        raise TypeError('sql must be type str, got %s' % type(sql))
    from pyhive import hive
    from TCLIService.ttypes import TOperationState
    cursor = hive.connect('HZ2-BG-1601-P018').cursor()
    cursor.execute(sql, async=True)
    status = cursor.poll().operationState
    while status in (TOperationState.INITIALIZED_STATE, TOperationState.RUNNING_STATE):
        logs = cursor.fetch_logs()
        for message in logs:
            logger.info(message)
        status = cursor.poll().operationState
    return cursor.fetchall()


if __name__ == "__main__":

    conf_info = get_conf_info()

    data_zz_iv = fetch_from_hive(conf_info["sql"])

    joblib.dump(data_zz_iv, "%s" % conf_info["raw_data_dump_path"])
    print(np.array(data_zz_iv).shape)