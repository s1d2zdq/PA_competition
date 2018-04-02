# coding: utf-8
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)

# TERMINALNO, TIME, TRIP_ID, LONGITUDE, LATITUDE, DIRECTION, HEIGHT, SPEED, CALLSTATE, Y

from conf.configure import Configure
from utils.data_utils import save_features

from functions.trip_id_count import wyj_trip_id_count
from functions.trip_id_interval_mean import wyj_trip_id_interval_mean
from functions.speed_variance_mean import wyj_speed_variance_mean
from functions.speed_final_mean import wyj_speed_final_mean
from functions.time_direction_change_feat import rxd_time_gap_direction_change_feat
from functions.callstate_feat import rxd_callstate_feat


def save_all_features(train, test):
    funcs = {
        'speed_variance_mean': wyj_speed_variance_mean,
        'trip_id_count': wyj_trip_id_count,
        'trip_id_interval_mean': wyj_trip_id_interval_mean,
        'speed_final_mean': wyj_speed_final_mean,
        'time_gap_direction_change_feat': rxd_time_gap_direction_change_feat,
        'callstate_feat': rxd_callstate_feat,
    }
    for name in Configure.features:
        save_features(*funcs[name](train, test), name)


if __name__ == "__main__":
    print("****************** feature **********************")
    # 程序入口
    # save_all_features()
