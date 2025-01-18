import os, re
import numpy  as np
import pandas as pd
# ---------- Compressed files------------------------------------------

import bz2
import _pickle as cPickle
# Pickle a file and then compress it into a file
def compressed_pickle(filepath_with_extension, picklable_data_structure):
    with bz2.BZ2File(filepath_with_extension, 'w') as f: 
        cPickle.dump(picklable_data_structure, f)
#compressed_pickle(path + '\\' + 'filename.pbzip2', data)

# Load any compressed pickle file
def decompress_pickle(filepath_with_extension):
    pickle_file = bz2.BZ2File(filepath_with_extension, 'rb')
    data = cPickle.load(pickle_file)
    return data

#data = decompress_pickle(path + '\\' + 'filename.pbzip2')

#========================================================================
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    
    volt_cloumns = ['V1', 'V10', 'V11', 'V12', 'V13', 'V14', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9']
    volt_cloumns.sort(key=natural_keys)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]
    
def get_files_list(data_dir = './', file_extension = None):
    files_list = os.listdir(data_dir)
    if file_extension:
        files_list = list(file_name for file_name in files_list \
                                 if file_name.endswith(file_extension))
    return files_list
    
def get_files_props_df(data_dir, file_extension = None):
    file_props_dicts_list = []
    files_list = get_files_list(data_dir, file_extension)
    for file_name in files_list:
        file_path = os.path.join(data_dir, file_name)
        if os.path.isfile(file_path):
            file_props_dict = {}
            file_props_dict['file_name'] = file_name
            #print(file_name, os.path.getsize(file_path))
            file_props_dict['size']      = os.path.getsize(file_path)
            file_props_dict['file_path'] = file_path
            file_props_dicts_list.append(file_props_dict)
    if file_props_dicts_list:
        return pd.DataFrame(file_props_dicts_list).sort_values(by = ['size'],
                                                   inplace        = False,
                                                   ascending      = False,
                                                   ignore_index   = True)
    else:
        return None
def get_Ah_kWh_hrs_maxA(curr_mA, pack_V_mV, diff_time_secs):
    calc_vals_dict = {}
    
    calc_vals_dict['energy_kWh']  = round(np.sum(curr_mA * diff_time_secs * pack_V_mV)/3600./1000./1000./1000., 2)
    calc_vals_dict['op_time']     = round(np.sum(diff_time_secs)/3600., 2)
    if len(curr_mA) > 0:
        calc_vals_dict['max_curr_A']  = round(np.max(curr_mA)/1000., 2)
        calc_vals_dict['cap_Ah']      = round(np.sum(curr_mA * diff_time_secs)/3600./1000., 2)
    else:
        calc_vals_dict['max_curr_A']  = None
        calc_vals_dict['cap_Ah']      = None

    return calc_vals_dict

    
def get_distance_gap(odometer_series, odometer_dict):
    odometer_series        = odometer_series.dropna()
    odometer_dict['start_odometer'] = odometer_series.iloc[0]
    odometer_dict['end_odometer']   = odometer_series.iloc[-1]
    odometer_dict['drive_distance'] = odometer_series.iloc[-1] - odometer_series.iloc[0]
    return odometer_dict
#-----------------------------------------------------------
def get_time_gap(timestamp_series):
    # suitable for one day data only
    start_time        = timestamp_series.iloc[0]
    end_time          = timestamp_series.iloc[-1]
    delta_time_pd     = pd.Timedelta(end_time - start_time, unit = 'ms')
    delta_time_secs   = delta_time_pd.total_seconds()
    delta_time_HHMMSS = pd.to_datetime(delta_time_secs, unit = 's').strftime("%H:%M:%S")
    delta_time_dict = {}
    delta_time_dict['delta_time_pd_timedelta'] = delta_time_pd
    delta_time_dict['delta_time_secs']         = delta_time_secs
    delta_time_dict['delta_time_HHMMSS']       = delta_time_HHMMSS
    return delta_time_dict
def get_diff_time(time_column):
    #time_dt_sec = np.diff(time_column)/ np.timedelta64(1, 's')
    time_dt_sec = np.diff(time_column).astype('timedelta64[s]').astype(np.int32)
    time_dt_sec = np.insert(time_dt_sec, 0, 1.)
    return time_dt_sec

def add_time_columns(data_df):
    data_df.sort_values(by  = [timestamp], inplace = True, ignore_index = True)
    data_df['utc_time']     = pd.to_datetime(data_df[timestamp], unit= 'ms', utc=True)
    data_df['indian_time']  = data_df['utc_time'].dt.tz_convert(indian_time)
    data_df['diff_time_s']  = get_diff_time(data_df['utc_time'])
    return data_df
#-----------------------------------------------------------
def add_fig2html(html_data, fig):
    tmpfile    = BytesIO()
    fig.savefig(tmpfile, format='webp', dpi=100, pad_inches = 0.02, bbox_inches = 'tight')
    encoded    = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html_data += '<img src=\'data:image/webp;base64,{}\'>'.format(encoded) + '<br>'
    plt.close()
    plt.show()
    return html_data
    
def NaN_zero_table(df, battery_ID):
    num_records      = len(df)
    # Zero values statistics
    zero_val_count   = (df == 0.00).astype(int).sum(axis=0)
    zero_val_percent = 100 * zero_val_count / num_records
    
    # NaN values statistics
    NaN_val_count    = df.isnull().sum()
    NaN_val_percent  = 100 * NaN_val_count / num_records
    
    NaN_zero_table = pd.concat([zero_val_count, zero_val_percent, NaN_val_count, NaN_val_percent], axis = 1)
    NaN_zero_table = NaN_zero_table.rename(columns = {0 : 'Zero Values', 1 : '% of Zeros', 2 : 'NaN Values', 3 : '% of NaN Values'})
    
    NaN_zero_table['Count Zero + NaN Values'] = NaN_zero_table['Zero Values'] + NaN_zero_table['NaN Values']
    NaN_zero_table['% Zero + NaN Values']     = 100 * NaN_zero_table['Count Zero + NaN Values'] / num_records
    #NaN_zero_table['Data Type']  = df.dtypes
    NaN_zero_table['vehicle_ID'] = battery_ID
    NaN_zero_table = NaN_zero_table[NaN_zero_table.iloc[:,1] != 0].sort_values(
                                                '% of NaN Values', ascending = False).round(1)
    #if NaN_zero_table.shape[0] > 0:
    #    print ("Battery: "+ battery_ID +"has " + str(df.shape[1]) + \
    #           " columns and " + str(df.shape[0]) + " Rows.\n"   + \
    #           "There are "    + str(NaN_zero_table.shape[0]) + " columns that have missing values.")
    #NaN_zero_table.to_excel('D:/sampledata/missing_and_zero_values.xlsx', freeze_panes=(1,0), index = False)
    return NaN_zero_table

#missing_zero_values_table(results)