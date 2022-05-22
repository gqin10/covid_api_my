import logging

import azure.functions as func
import pandas as pd
import json


def main(req: func.HttpRequest) -> str:
    data = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_malaysia.csv')
    day = req.params.get('day')
    data = data.loc[data['date'].isin((data['date'].unique())[-30 if not day else -int(day):])]

    return json.dumps({
        'labels': (data['date']).to_list(),
        'data_new_case': (data['cases_new']).to_list(),
        'data_recover_case': (data['cases_recovered']).to_list()
    })