
def get_settings(exp_name):
    
    exps = {
                'WRF_jan_init': {
                        'WRF_dir'            : '/Users/ngordillo/WRFPLUSV3/test/',
                        'box_size'           : 5,


                        'run_hours'          : "48",
                        'start_year'           : "2026",
                        'start_month'          : "01",
                        'start_day'            : "30",
                        'start_hour'           : "12",
                        'end_year'             : "2026",
                        'end_month'            : "02",
                        'end_day'              : "01",
                        'end_hour'             : "12",
                        'time_step'           : "60",                 
                       },
                'WRF_Florence_test': {
                        'WRF_dir'            : '/Users/ngordillo/florence/',
                        'adj_jc'             : 119,
                        'adj_ic'             : 181,
                        'box_size'           : 10,

                        #NAMELIST INFO
                        'run_hours'          : "36",
                        'start_year'           : "2018",
                        'start_month'          : "09",
                        'start_day'            : "09",
                        'start_hour'           : "00",
                        'end_year'             : "2018",
                        'end_month'            : "09",
                        'end_day'              : "10",
                        'end_hour'             : "12",
                        'interval_seconds'   : "3600",
                        'interval_seconds_adj'    : "10800",
                        'time_step'           : "60",
                        'e_we'               : 350,
                        'e_sn'               : 240,
                        'dx'                 : 18000,
                        'dy'                 : 18000,

                        'dresponse_value'     : -150,              
                       },
                'WRF_Florence_test2': {
                        'WRF_dir'            : '/Users/ngordillo/florence/',
                        'adj_jc'             : 119,
                        'adj_ic'             : 181,
                        'box_size'           : 10,

                        #NAMELIST INFO
                        'run_hours'          : "36",
                        'start_year'           : "2018",
                        'start_month'          : "09",
                        'start_day'            : "09",
                        'start_hour'           : "00",
                        'end_year'             : "2018",
                        'end_month'            : "09",
                        'end_day'              : "10",
                        'end_hour'             : "12",
                        'time_step'           : "60",
                        'e_we'               : 350,
                        'e_sn'               : 240,
                        'dx'                 : 18000,
                        'dy'                 : 18000,                     
                       },
    }

    return exps[exp_name]
  