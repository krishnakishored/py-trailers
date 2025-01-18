#!/usr/bin/env python
# coding: utf-8

import os, sys, time, pickle, datetime, re, io, pytz

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MinuteLocator
import pandas as pd
from pandas.core.tools.datetimes import _guess_datetime_format_for_array
import plotly.express as px
from os.path import isfile, join
import openpyxl
import xlwings
import bz2
import _pickle as cPickle
from scipy.stats.mstats import winsorize
from functools import reduce
from IPython.display import display, HTML
import tabulate
import warnings
from importlib import reload
import eChargeUp_utils

reload(eChargeUp_utils)
# ............Instructions.......................
# 1. before running the script create image folder to save ivt profiles
# ===========================================================

time_ticks = DateFormatter("%H:%M", tz=pytz.timezone("Asia/Kolkata"))

indian_time_tz = pytz.timezone("Asia/Kolkata")
time_ticks = DateFormatter("%H:%M", tz=indian_time_tz)

min_Num_data_points = 50  # Num of data points reqd to determine data is sufficient for Battery analytics

max_disconnexn_time_secs = 300.1
plot_graphs = True


root_dir_chargeup_data = "D:/nunam_project/Nunam_Recent_Projects/code/new_customer_packs_data/data/charg-up"
output_data_dir = "D:/nunam_project/Nunam_Recent_Projects/code/new_customer_packs_data/data/charg-up/output"


batt_data_columns = [
    "timestamp",
    "Ip",
    "Vp",
    "SoC",
    "V1",
    "V2",
    "V3",
    "V4",
    "V5",
    "V6",
    "V7",
    "V8",
    "V9",
    "V10",
    "V11",
    "V12",
    "V13",
    "V14",
    "V15",
    "V16",
    "T1",
    "T2",
    "T3",
    "T4",
    "power",
    "load_status",
    "allow_charging",
    "allow_discharging",
]
float_cols = [
    "Ip",
    "Vp",
    "SoC",
    "V1",
    "V2",
    "V3",
    "V4",
    "V5",
    "V6",
    "V7",
    "V8",
    "V9",
    "V10",
    "V11",
    "V12",
    "V13",
    "V14",
    "V15",
    "V16",
    "T1",
    "T2",
    "T3",
    "T4",
    "power",
    "load_status",
    "allow_charging",
    "allow_discharging",
]
int_cols = []


# # Process Battery Data

batt_alerts_columns = [
    "timestamp",
    "alert_pack_ov_fault_total_pack_voltage_is_higher_than_set_threshold",
    "alert_cell_conn_broken",
    "alert_cell_under_voltage_discharged",
    "alert_thermal_runaway",
    "alert_over_current_charging",
    "alert_over_temp",
    "alert_cell_over_voltage_charged",
    "alert_cell_diff_fault_battery_is_disbalanced",
    "alert_board_over_temp",
    "alert_prl_fault_fault_in_battery_connected_in_parallel",
    "alert_board_under_temp",
    "alert",
    "alert_under_temp",
    "alert_over_current_cont_charging",
    "alert_over_current_discharging",
]

driv_data_columns = [
    "timestamp",
    "lat",
    "lon",
    "speed",
    "alt",
    "odometer",
    "internal_battery_voltage",
]

batt_data_columns = [
    "timestamp",
    "Ip",
    "Vp",
    "SoC",
    "V1",
    "V2",
    "V3",
    "V4",
    "V5",
    "V6",
    "V7",
    "V8",
    "V9",
    "V10",
    "V11",
    "V12",
    "V13",
    "V14",
    "V15",
    "V16",
    "T1",
    "T2",
    "T3",
    "T4",
    "power",
    "load_status",
    "allow_charging",
    "allow_discharging",
]

summary_columns = ["cycle_count", "SoH"]
fixed_columns = ["chemistry", "bms_id", "battery_capacity"]

unimportant_columns = [
    "ts_kafka",
    "bat_id_1",
    "bat_id_13",
    "bat_id_14",
    "bat_id_15",
    "bat_id_16",
    "status",
    "heading",
    "numsatu",
]


pack_voltage = "Vp"
pack_current = "Ip"
pack_chg_current = "ic"
pack_dischg_current = "id"
pack_temperature = "T4"
pack_SOC = "SoC"
timestamp = "timestamp"
indian_timestamp = "Indian_timestamp"  # The timestamp column will be renamed as Indian_timestamp without tzaware.
utc_timestamp = "utc_timestamp"
indian_time = "indian_time"
charging_state = "charging"
discharging_state = "running"
idle_state = "idle"

# str_volt_columns = list(col_name for col_name in veh_df.columns if 'strv_' in col_name)
str_volt_columns = [
    "V1",
    "V2",
    "V3",
    "V4",
    "V5",
    "V6",
    "V7",
    "V8",
    "V9",
    "V10",
    "V11",
    "V12",
    "V13",
    "V14",
    "V15",
    "V16",
]
# Removed strings 1 as the data is not in post-processed csv files
str_volt_columns = [
    "V2",
    "V3",
    "V4",
    "V5",
    "V6",
    "V7",
    "V8",
    "V9",
    "V10",
    "V11",
    "V12",
    "V13",
    "V14",
    "V15",
    "V16",
]


def get_reqd_df_cols(df, reqd_cols):
    reqd_data_cols = list(set(reqd_cols).intersection(set(df.columns)))
    cols_check_list = reqd_data_cols.copy()
    cols_check_list.remove(timestamp)
    if len(cols_check_list) != 0:
        new_df = df.loc[df[cols_check_list].notnull().any(axis=1)][
            reqd_data_cols
        ].copy(deep=True)
        missing_cols = list(set(reqd_cols) - set(new_df.columns))
        if len(missing_cols) == 0:
            missing_cols = "No missinng columns"
    else:
        new_df = None
        missing_cols = "All Columns Missing"
    return new_df, missing_cols


def add_time_columns(data_df):
    # Timestamp column is timezone unaware but shows Indian time
    # timezone conversion function takes in UTC timestamp series only
    # Plots timeticks are enabled for timezone aware datetime in column: 'indian_time'.
    # We are creating timezone awarenesss in a roundabout way
    data_df.sort_values(by=[timestamp], inplace=True, ignore_index=True)
    data_df.rename(
        columns={timestamp: indian_timestamp}, inplace=True
    )  # timezone unaware indian_timestamp
    utc_timestamp = data_df[indian_timestamp] - pd.Timedelta("330min")
    utc_time = pd.to_datetime(utc_timestamp, unit="ms", utc=True)
    data_df["indian_time"] = utc_time.dt.tz_convert(
        indian_time_tz
    )  # timezone aware Indian datetime

    diff_time_secs = eChargeUp_utils.get_diff_time(data_df["indian_time"])
    data_df["diff_time_secs"] = diff_time_secs

    return data_df


def get_battery_state(row):
    if row["load_status"] == 4.0:
        return charging_state
    if row["load_status"] == 3.0:
        return discharging_state
    return idle_state


def get_sessions_df(veh_batt_df):
    sessions_list = []
    for session_id in veh_batt_df["session_id"].unique():
        temp_df = veh_batt_df[veh_batt_df["session_id"] == session_id]
        temp_dict = temp_df[["state", "session_id"]].iloc[0].to_dict()

        temp_dict["num_records"] = temp_df.shape[0]
        temp_dict["start_time"] = temp_df["indian_time"].iloc[0]
        temp_dict["end_time"] = temp_df["indian_time"].iloc[-1]
        # addding Ah_kWh_hrs_maxA_session wise
        session_Ah_kWh_hrs_maxA_dict = {}
        if temp_df["state"].isin([charging_state, discharging_state]).any():
            pack_V_array_mV = temp_df[pack_voltage].values
            curr_array_mA = temp_df[pack_current].values
            diff_time_secs = temp_df["diff_time_secs"].values
            diff_time_secs = np.where(
                diff_time_secs < 60.1, diff_time_secs, 1.0
            )
            session_Ah_kWh_hrs_maxA_dict = eChargeUp_utils.get_Ah_kWh_hrs_maxA(
                curr_array_mA, pack_V_array_mV, diff_time_secs
            )

        ##
        temp_dict["session_delta_time_secs"] = np.sum(
            temp_df["diff_time_secs"].values
        )
        temp_dict["session_Ah_kWh_hrs_maxA_dict"] = (
            session_Ah_kWh_hrs_maxA_dict
        )

        sessions_list.append(temp_dict)

    sessions_df = pd.DataFrame(sessions_list)
    # display(sessions_df['state'].value_counts())
    return sessions_df


def include_disconnexn_state(sessions_df):
    sessions_df["session_gap_time"] = (
        sessions_df.shift(-1)["start_time"] - sessions_df["end_time"]
    ).astype("timedelta64[s]")
    sessions_df["next_state"] = sessions_df.shift(-1)["state"]
    sessions_df["next_state_start_time"] = sessions_df.shift(-1)["start_time"]

    disconnexn_dicts_list = []
    for index, row_data in sessions_df.iterrows():
        # if (row_data['state'] == idle_state) & (row_data['next_state'] == idle_state):
        #    continue

        if (
            row_data["session_gap_time"].total_seconds()
            > max_disconnexn_time_secs
        ):
            disconnexn_dict = {}
            disconnexn_dict["state"] = "disconnection"
            disconnexn_dict["num_records"] = 0
            disconnexn_dict["start_time"] = row_data[
                "end_time"
            ] + pd.Timedelta("1s")
            disconnexn_dict["end_time"] = row_data[
                "next_state_start_time"
            ] - pd.Timedelta("1s")
            disconnexn_dict["session_delta_time_secs"] = (
                disconnexn_dict["end_time"] - disconnexn_dict["start_time"]
            ).total_seconds()
            # print(row_data['session_gap_time'].total_seconds())
            disconnexn_dicts_list.append(disconnexn_dict)
    disconnexn_df = pd.DataFrame(disconnexn_dicts_list)
    reqd_cols_list = [
        "state",
        "num_records",
        "start_time",
        "end_time",
        "session_delta_time_secs",
        "session_Ah_kWh_hrs_maxA_dict",
    ]
    if disconnexn_df.empty:
        new_sessions_df = pd.concat(
            [sessions_df[reqd_cols_list], disconnexn_df]
        )
        new_sessions_df = new_sessions_df.sort_values(
            by=["start_time"], ignore_index=True
        )
    else:
        new_sessions_df = sessions_df[reqd_cols_list]
    return new_sessions_df


def get_state_session_id(summary_dict, veh_batt_df):
    veh_batt_df["state"] = veh_batt_df.apply(get_battery_state, axis=1)
    diff_state = veh_batt_df["state"] != veh_batt_df["state"].shift(1)
    # veh_batt_df['session_id'] = (diff_state).cumsum()

    gt_5min = veh_batt_df[indian_timestamp].diff() > pd.Timedelta("5min")
    veh_batt_df["session_id"] = (diff_state | gt_5min).cumsum()

    sessions_df = get_sessions_df(veh_batt_df)
    # Regen braking session
    sessions_df["state"] = np.where(
        (
            (sessions_df["state"] == charging_state)
            & (
                sessions_df["state"]
                .shift(-1)
                .isin([discharging_state, idle_state])
            )
            & (
                sessions_df["state"]
                .shift(1)
                .isin([discharging_state, idle_state])
            )
            & (sessions_df["num_records"] <= 3)
        ),
        discharging_state,
        sessions_df["state"],
    )

    sessions_df["state"] = np.where(
        (
            (sessions_df["state"] == idle_state)
            & (sessions_df["state"].shift(-1) == discharging_state)
            & (sessions_df["state"].shift(1) == discharging_state)
        ),
        np.where(
            sessions_df["session_delta_time_secs"] <= 1199.0,
            discharging_state,
            sessions_df["state"],
        ),
        sessions_df["state"],
    )

    veh_batt_df = veh_batt_df.set_index("session_id")
    sessions_df = sessions_df.set_index("session_id")

    veh_batt_df.update(sessions_df)
    veh_batt_df.reset_index(inplace=True)

    diff_state = veh_batt_df["state"] != veh_batt_df["state"].shift(1)

    # gt_5min_nonidle_state = (df[indian_timestamp].diff() > pd.Timedelta("5min")) & (df['state'] != idle_state)
    # veh_batt_df['session_id']   = (diff_state | gt_5min_nonidle_state).cumsum()

    gt_5min = veh_batt_df[indian_timestamp].diff() > pd.Timedelta("5min")
    veh_batt_df["session_id"] = (diff_state | gt_5min).cumsum()

    sessions_df = get_sessions_df(veh_batt_df)
    summary_dict["sessions_df"] = include_disconnexn_state(sessions_df)
    return summary_dict, veh_batt_df


def get_Ah_kWh_hrs_maxA(curr_mA, pack_V_mV, diff_time_secs):
    calc_vals_dict = {}
    calc_vals_dict["op_time"] = round(np.sum(diff_time_secs) / 3600.0, 2)
    if len(curr_mA) > 0:
        calc_vals_dict["max_curr_A"] = round(np.max(curr_mA) / 1000.0, 2)
        calc_vals_dict["mean_curr_A"] = round(np.mean(curr_mA) / 1000.0, 2)
        calc_vals_dict["cap_Ah"] = round(
            np.sum(curr_mA * diff_time_secs) / 3600.0 / 1000.0, 2
        )
        calc_vals_dict["energy_kWh"] = round(
            np.sum(curr_mA * diff_time_secs * pack_V_mV)
            / 3600.0
            / 1000.0
            / 1000.0
            / 1000.0,
            2,
        )
    else:
        calc_vals_dict["max_curr_A"] = None
        calc_vals_dict["mean_curr_A"] = None
        calc_vals_dict["cap_Ah"] = None
        calc_vals_dict["energy_kWh"] = None

    return calc_vals_dict


def get_dischg_usage_vals(dischg_df, batt_usagevals_dict):
    if pack_dischg_current in dischg_df.columns:
        pack_V_array_mV = dischg_df[pack_voltage]
        curr_array_mA = dischg_df[pack_dischg_current].values

        diff_time_secs = dischg_df["diff_time_secs"].values
        diff_time_secs = np.where(diff_time_secs < 60.1, diff_time_secs, 1.0)

        calc_vals_dict = get_Ah_kWh_hrs_maxA(
            curr_array_mA, pack_V_array_mV, diff_time_secs
        )

        batt_usagevals_dict["dischg_cap_Ah"] = calc_vals_dict["cap_Ah"]
        batt_usagevals_dict["dischg_ergy_kWh"] = calc_vals_dict["energy_kWh"]
        batt_usagevals_dict["dischg_time_Hrs"] = calc_vals_dict["op_time"]
        batt_usagevals_dict["dischg_max_curr_Amps"] = calc_vals_dict[
            "max_curr_A"
        ]
        batt_usagevals_dict["dischg_mean_curr_Amps"] = calc_vals_dict[
            "mean_curr_A"
        ]
        if calc_vals_dict["cap_Ah"] is None:
            batt_usagevals_dict["dischg_FCE"] = None
        else:
            batt_usagevals_dict["dischg_FCE"] = (
                calc_vals_dict["cap_Ah"] / 100.0
            )
    else:
        batt_usagevals_dict["dischg_cap_Ah"] = None
        batt_usagevals_dict["dischg_ergy_kWh"] = None
        batt_usagevals_dict["dischg_time_Hrs"] = None
        batt_usagevals_dict["dischg_max_curr_Amps"] = None
        batt_usagevals_dict["dischg_mean_curr_Amps"] = None
        batt_usagevals_dict["dischg_FCE"] = None
    return batt_usagevals_dict


def get_chg_usage_vals(chg_df, batt_usagevals_dict):
    if pack_chg_current in chg_df.columns:
        # pack_V_array_mV = chg_df[str_volt_columns].sum(axis = 1)
        pack_V_array_mV = chg_df[pack_voltage]
        curr_array_mA = chg_df[pack_chg_current].values

        diff_time_secs = chg_df["diff_time_secs"].values
        diff_time_secs = np.where(diff_time_secs < 60.1, diff_time_secs, 1.0)

        calc_vals_dict = get_Ah_kWh_hrs_maxA(
            curr_array_mA, pack_V_array_mV, diff_time_secs
        )

        batt_usagevals_dict["chg_cap_Ah"] = calc_vals_dict["cap_Ah"]
        batt_usagevals_dict["chg_ergy_kWh"] = calc_vals_dict["energy_kWh"]
        batt_usagevals_dict["chg_time_Hrs"] = calc_vals_dict["op_time"]
        batt_usagevals_dict["chg_max_curr_Amps"] = calc_vals_dict["max_curr_A"]
        batt_usagevals_dict["chg_mean_curr_Amps"] = calc_vals_dict[
            "mean_curr_A"
        ]
        if calc_vals_dict["cap_Ah"] is None:
            batt_usagevals_dict["chg_FCE"] = None
        else:
            batt_usagevals_dict["chg_FCE"] = calc_vals_dict["cap_Ah"] / 100.0
    else:
        batt_usagevals_dict["chg_cap_Ah"] = None
        batt_usagevals_dict["chg_ergy_kWh"] = None
        batt_usagevals_dict["chg_time_Hrs"] = None
        batt_usagevals_dict["chg_max_curr_Amps"] = None
        batt_usagevals_dict["chg_mean_curr_Amps"] = None
        batt_usagevals_dict["chg_FCE"] = None
    return batt_usagevals_dict


def get_percentage_gap(energy_series):
    mean_energy = np.mean(winsorize(energy_series, limits=[0.25, 0.25]))
    return (energy_series - mean_energy) / mean_energy * 100.0


def get_stringwise_energy(summary_dict, df):
    selected_str_volt_columns = list(
        set(str_volt_columns).intersection(set(df.columns))
    )
    chg_df = df[df["state"] == charging_state]
    chg_string_power = chg_df[selected_str_volt_columns].multiply(
        chg_df[pack_chg_current], axis=0
    )
    diff_time_secs = chg_df["diff_time_secs"].copy(deep=True)
    diff_time_secs.loc[diff_time_secs >= max_disconnexn_time_secs] = 1.0
    chg_string_energy = chg_string_power.multiply(diff_time_secs, axis=0)
    chg_string_energy = (
        chg_string_energy.sum(axis=0) / 3600.0 / 1000.0 / 1000.0
    )

    dischg_df = df[df["state"] == discharging_state]
    dischg_string_power = dischg_df[selected_str_volt_columns].multiply(
        dischg_df[pack_dischg_current], axis=0
    )
    diff_time_secs = dischg_df["diff_time_secs"].copy(deep=True)
    diff_time_secs.loc[diff_time_secs >= max_disconnexn_time_secs] = 1.0

    dischg_string_energy = dischg_string_power.multiply(diff_time_secs, axis=0)
    dischg_string_energy = (
        dischg_string_energy.sum(axis=0) / 3600.0 / 1000.0 / 1000.0
    )

    string_Ergy_df = pd.DataFrame(
        {
            "string_num": pd.Series(selected_str_volt_columns),
            "chg_ergy_Wh": pd.Series(chg_string_energy.to_list()),
            "dischg_ergy_Wh": pd.Series(dischg_string_energy.to_list()),
        }
    )

    if string_Ergy_df["chg_ergy_Wh"].all() == 0:
        string_Ergy_df["chg_ergy_%gap"] = pd.Series(
            [0.0] * len(string_Ergy_df["chg_ergy_Wh"].values)
        )
    else:
        string_Ergy_df["chg_ergy_%gap"] = pd.Series(
            get_percentage_gap(string_Ergy_df["chg_ergy_Wh"]).to_list()
        )

    if string_Ergy_df["dischg_ergy_Wh"].all() == 0:
        string_Ergy_df["dischg_ergy_%gap"] = pd.Series(
            [0.0] * len(string_Ergy_df["dischg_ergy_Wh"].values)
        )
    else:
        string_Ergy_df["dischg_ergy_%gap"] = pd.Series(
            get_percentage_gap(string_Ergy_df["dischg_ergy_Wh"]).to_list()
        )

    string_Ergy_df["abs_%ergy_gap"] = np.abs(
        string_Ergy_df["chg_ergy_%gap"]
    ) + np.abs(string_Ergy_df["dischg_ergy_%gap"])
    string_Ergy_df["%ergy_gap"] = (
        string_Ergy_df["chg_ergy_%gap"] + string_Ergy_df["dischg_ergy_%gap"]
    )

    string_Ergy_df = string_Ergy_df[
        ~(string_Ergy_df["abs_%ergy_gap"].isnull())
    ]
    max_Erggap_string = string_Ergy_df.loc[
        string_Ergy_df["abs_%ergy_gap"].idxmax()
    ]

    summary_dict["max_abs_%Ergy_gap"] = max_Erggap_string["abs_%ergy_gap"]
    summary_dict["max_abs_%Ergy_gap_string"] = max_Erggap_string["string_num"]
    summary_dict["string_Ergy_df"] = string_Ergy_df

    a = string_Ergy_df[
        "abs_%ergy_gap"
    ].values  # Plot scatter pct energy gap between strings
    if np.any(a[a > 0.0]):
        # display(summary_dict['vehicle_ID'], string_Ergy_df.round(2))
        plt.scatter(
            string_Ergy_df["chg_ergy_Wh"].values,
            string_Ergy_df["dischg_ergy_Wh"].values,
        )
        plt.xlabel("Charge Energy [Wh]", fontsize=14)
        plt.ylabel("Discharge Energy [Wh]", fontsize=14)
        plt.title("Stringwise Energy Ratio", fontsize=16)
        plt.grid(True, linestyle=":", linewidth=0.6)
        plt.close()

    return summary_dict, string_Ergy_df


## Make plots of each vehicle
def make_veh_batt_usage_plot(vehicle_ID, date_string, veh_df, html_data):
    selected_str_volt_columns = list(
        set(str_volt_columns).intersection(set(veh_df.columns))
    )
    ax_titles_list = ["V", "current"]
    ax_ylabels_list = ["string V [mV]", "current [A]"]

    dischg_df = veh_df[veh_df["state"] == discharging_state]
    chg_df = veh_df[veh_df["state"] == charging_state]

    fig, ax = plt.subplots(3, 1, figsize=(16, 9))

    pack_ax_11 = ax[0]
    pack_ax_21 = ax[1]

    x_axis_vals = veh_df["indian_time"].values

    pack_ax_11.plot(x_axis_vals, veh_df[selected_str_volt_columns[:]].values)
    pack_ax_21.plot(
        x_axis_vals, veh_df[pack_chg_current].values / 1000.0, c="r"
    )
    pack_ax_21.plot(
        x_axis_vals, -veh_df[pack_dischg_current].values / 1000.0, c="g"
    )

    for plot_ax, ax_ylabel, ax_title in zip(
        ax, ax_ylabels_list, ax_titles_list
    ):
        plot_ax.set_ylabel(ax_ylabel, fontsize=12)
        plot_ax.set_title(ax_title, fontsize=12, y=1.0, pad=-14, loc="right")
        plot_ax.grid(True, linestyle=":", linewidth=0.4)
        plot_ax.xaxis.set_major_formatter(time_ticks)
        plot_ax.xaxis.set_tick_params(rotation=30, labelsize=10)

    SOC_ax = pack_ax_11.twinx()
    SOC_ax.plot(x_axis_vals, veh_df[pack_SOC].values, linewidth=2, c="C3")
    SOC_ax.set_ylabel("BMS SOC", fontsize=12, color="C3", fontweight="bold")
    SOC_ax.tick_params(axis="y", labelcolor="C3", labelsize=12)

    pack_V_ax = ax[2]
    plot_df = veh_df  # [~(veh_batt_df['state']== charging_state)]
    marker_color_map = np.where(
        plot_df["state"] == charging_state,
        "r",
        np.where(plot_df["state"] == discharging_state, "b", "y"),
    )

    pack_V_ax.scatter(
        plot_df["indian_time"], plot_df[pack_voltage], c=marker_color_map
    )
    pack_V_ax.xaxis.set_major_formatter(time_ticks)
    pack_V_ax.xaxis.set_tick_params(rotation=30, labelsize=10)
    pack_V_ax.set_ylabel("Pack Voltage")
    # session_ax = ax.twinx()
    # session_ax.plot(plot_df['indian_time'].values, plot_df['session_id'].values, 'o')
    # session_ax.set_ylabel('Session ID')
    pack_V_ax.grid(True, linestyle=":", linewidth=0.4)

    fig.suptitle(vehicle_ID + "_" + date_string)
    fig.tight_layout()
    # fig.savefig('./images/'+vehicle_ID+'_'+ date_string+'.jpg', dpi = 100, pad_inches = 0.02, bbox_inches = 'tight')
    html_data = eChargeUp_utils.add_fig2html(html_data, fig, vehicle_ID)
    plt.close()
    return html_data

    # plt.show()


def get_batt_summary_dict(summary_dict, batt_df):
    batt_df = add_time_columns(batt_df)
    # battery summary
    summary_dict["batt_telemetry_count"] = batt_df.shape[0]
    selected_float_cols = list(
        set(float_cols).intersection(set(batt_df.columns))
    )
    for col_name in selected_float_cols:
        batt_df[col_name] = batt_df[col_name].astype(float)
    if pack_voltage in batt_df.columns:
        batt_df[pack_voltage] = batt_df[pack_voltage] * 1000.0
    selected_str_volt_columns = list(
        set(str_volt_columns).intersection(set(batt_df.columns))
    )
    batt_df[selected_str_volt_columns] = (
        batt_df[selected_str_volt_columns] * 1000.0
    )
    ## change the name according to unit
    if pack_current in batt_df.columns:
        batt_df[pack_current] = batt_df[pack_current] * 1000.0

    # Creating charge current column and discharge column from pack current column
    batt_df[pack_chg_current] = 0.0
    batt_df[pack_dischg_current] = 0.0

    batt_df.loc[batt_df["load_status"] == 4.0, pack_chg_current] = batt_df.loc[
        batt_df["load_status"] == 4.0, pack_current
    ].values
    batt_df.loc[~(batt_df["load_status"] == 4.0), pack_dischg_current] = (
        batt_df.loc[~(batt_df["load_status"] == 4.0), pack_current].values
    )
    # Create Sessions
    summary_dict, batt_df = get_state_session_id(summary_dict, batt_df)

    # Charge Discharge Statistics
    if pack_dischg_current in batt_df.columns:
        dischg_batt_df = batt_df[batt_df["state"] == discharging_state]
        summary_dict = get_dischg_usage_vals(dischg_batt_df, summary_dict)

    if pack_chg_current in batt_df.columns:
        chg_batt_df = batt_df[batt_df["state"] == charging_state]
        summary_dict = get_chg_usage_vals(chg_batt_df, summary_dict)

    diff_time_secs = batt_df["diff_time_secs"]
    summary_dict["missing_data_mins"] = (
        np.sum(diff_time_secs[diff_time_secs > max_disconnexn_time_secs])
        / 60.0
    )
    summary_dict["idle_time_hrs"] = 24.0 - (
        summary_dict["dischg_time_Hrs"]
        + summary_dict["chg_time_Hrs"]
        - summary_dict["missing_data_mins"] / 60.0
    )
    # Get string Imbalance
    summary_dict, string_Ergy_batt_df = get_stringwise_energy(
        summary_dict, batt_df
    )
    summary_dict["batt_df"] = batt_df
    return summary_dict


# Process day's vehicle's drive & GPS data
def get_driv_summary_dict(summary_dict, driv_df):
    driv_df = add_time_columns(driv_df)
    summary_dict["driv_telemetry_count"] = driv_df.shape[0]
    driv_df["odometer"] = driv_df["odometer"].astype(float)
    summary_dict = eChargeUp_utils.get_distance_gap(
        driv_df["odometer"], summary_dict
    )

    summary_dict["driv_df"] = driv_df
    return summary_dict


def process_daily_data(root_dir_chargeup_data, reqd_date_dir, html_data):
    batt_data_dir = root_dir_chargeup_data + "/" + reqd_date_dir
    # print(batt_data_dir)

    no_batt_data_dict_list = []
    veh_batt_summary_dicts_list = []
    for file_path in Path(batt_data_dir).iterdir():
        # ---------Trick to Ignore Green Cell bus data
        if file_path.name.lower().startswith("green"):
            continue
        # if file_name != 'CGF24D0016.parquet': continue # Trick to make it work for single file only
        # -----------------
        # print(file_name)
        df = pd.read_parquet(batt_data_dir + "/" + file_name)
        # ------------ Empty DataFrame Handling
        if df.empty:
            no_batt_cols_dict = {}
            no_batt_cols_dict["file_name"] = file_name
            no_batt_cols_dict["date"] = reqd_date_dir
            no_batt_data_dict_list.append(no_batt_cols_dict)
            continue
        # ------------
        df[timestamp] = df[timestamp].astype("datetime64[ms]")
        vehicle_ID = file_name.stem
        print("Calculation start:", vehicle_ID)
        # Splits df to 3 dataframe copies while retaining timestamp column in each
        batt_df, missing_batt_cols = get_reqd_df_cols(df, batt_data_columns)
        alerts_df, missing_alerts_cols = get_reqd_df_cols(
            df, batt_alerts_columns
        )
        driv_df, missing_driv_cols = get_reqd_df_cols(df, driv_data_columns)

        summary_dict = {}
        summary_dict["vehicle_ID"] = vehicle_ID
        summary_dict["date"] = reqd_date_dir
        summary_dict["missing_alerts_cols"] = missing_alerts_cols
        summary_dict["missing_batt_cols"] = missing_batt_cols
        summary_dict["missing_driv_cols"] = missing_driv_cols

        # ----------------------------------
        if not alerts_df is None:
            if not alerts_df.empty:
                alerts_df = add_time_columns(alerts_df)
                alerts_df = eChargeUp_utils.process_alerts(
                    alerts_df, batt_alerts_columns[1:]
                )
                summary_dict["alerts_df"] = alerts_df

        if not batt_df is None:
            if not batt_df.empty:
                summary_dict = get_batt_summary_dict(summary_dict, batt_df)
                if plot_graphs == True:
                    html_data = make_veh_batt_usage_plot(
                        vehicle_ID,
                        reqd_date_dir,
                        summary_dict["batt_df"],
                        html_data,
                    )
        if not driv_df is None:
            if not driv_df.empty:
                summary_dict = get_driv_summary_dict(summary_dict, driv_df)

        veh_batt_summary_dicts_list.append(summary_dict)

    no_batt_cols_vehs_df = pd.DataFrame(no_batt_data_dict_list)
    vehs_batt_summary_df = pd.DataFrame(veh_batt_summary_dicts_list)
    missing_cols_vehs_df = vehs_batt_summary_df[
        [
            "vehicle_ID",
            "date",
            "missing_batt_cols",
            "missing_alerts_cols",
            "missing_driv_cols",
        ]
    ]
    return (
        vehs_batt_summary_df,
        no_batt_cols_vehs_df,
        missing_cols_vehs_df,
        html_data,
    )


# -------------------------------------
def write_dfs_to_tabs(xl_writer, df_sheetname_tuples_list):
    for df, sheet_name in df_sheetname_tuples_list:
        if not df.empty:
            df.to_excel(
                xl_writer, sheet_name=sheet_name, startrow=1, startcol=1
            )
    return xl_writer


# -----------------------------------------------------------


# ..................main code starts from here.............................................................

reqd_date_dir = "2024-07-18"  #'2024-07-01'
save_dir = output_data_dir + "/" + reqd_date_dir
# Initialize HTML data
html_data = "<html><body>"
vehs_batt_summary_df, no_batt_cols_vehs_df, missing_cols_vehs_df, html_data = (
    process_daily_data(root_dir_chargeup_data, reqd_date_dir, html_data)
)
# ...........
with open("figure.html", "w") as file:
    file.write(html_data)
print("HTML file saved as figure.html")
data = {}
data["no_batt_cols_vehs_df"] = no_batt_cols_vehs_df
data["missing_cols_vehs_df"] = missing_cols_vehs_df
data["vehs_batt_summary_df"] = vehs_batt_summary_df

# ...Exporting compresses pickle file loaded with all calculation data
eChargeUp_utils.compressed_pickle(
    "./" + reqd_date_dir + "_veh_data_summary.pbzip2", data
)
with open("figure.html", "w") as file:
    file.write(html_data)
# .........Exporting Imprtant_columns from veh_data_summery in Excel format........................
reqd_excel_columns = [
    "vehicle_ID",
    "start_odometer",
    "end_odometer",
    "drive_distance",
    "batt_telemetry_count",
    "dischg_cap_Ah",
    "dischg_ergy_kWh",
    "dischg_time_Hrs",
    "dischg_max_curr_Amps",
    "dischg_mean_curr_Amps",
    "dischg_FCE",
    "chg_cap_Ah",
    "chg_ergy_kWh",
    "chg_time_Hrs",
    "chg_max_curr_Amps",
    "chg_mean_curr_Amps",
    "chg_FCE",
    "missing_data_mins",
    "idle_time_hrs",
    "max_abs_%Ergy_gap",
    "max_abs_%Ergy_gap_string",
    "date",
]

xl_file_path = "./" + reqd_date_dir + "_veh_data_limited_summary.xlsx"
xl_writer = pd.ExcelWriter(xl_file_path, engine="xlsxwriter")

# list of tuples of dataframe and xl_sheet_name
df_sheetname_tuples_list = [
    (vehs_batt_summary_df[reqd_excel_columns], "batt_usage_summary"),
    (no_batt_cols_vehs_df, "No_battery_data"),
    (missing_cols_vehs_df, "Missing_batt_data_columns"),
]

xl_writer = write_dfs_to_tabs(xl_writer, df_sheetname_tuples_list)
xl_writer.close()

# =======================main  code ends here======================================================
