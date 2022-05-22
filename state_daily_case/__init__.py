import logging

import azure.functions as func
import pandas as pd
import json


def main(req: func.HttpRequest) -> str:
    data = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_state.csv')
    day = req.params.get('day')
    state = req.params.get('state')
    
    date = (data['date'].unique())[-30 if not day else -int(day):]
    data = data[data['date'].isin(date)]

    data = data[data['state'] == state]
    return json.dumps({
        'labels': (data['date']).to_list(),
        'data_new_case': (data['cases_new']).to_list(),
        'data_recover_case': (data['cases_recovered']).to_list(),
        'data_0_11': (data['cases_0_4'] + data['cases_5_11']).to_list(),
        'data_12_17': (data['cases_12_17']).to_list(),
        'data_18_39': (data['cases_18_29'] + data['cases_30_39']).to_list(),
        'data_40_59': (data['cases_40_49'] + data['cases_50_59']).to_list(),
        'data_60': (data['cases_60_69'] + data['cases_70_79'] + data['cases_80']).to_list()
    })