import logging
import pandas as pd
import azure.functions as func
import json


def main(req: func.HttpRequest) -> str:

    data = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/deaths_state.csv')
    day = req.params.get('day')
    state = req.params.get('state')
    data = data[data['state'] == state]
    data = data.loc[:,['date','state','deaths_new_dod']]

    date = (data['date'].unique())[-30 if not day else -int(day):]
    data = data[data['date'].isin(date)]

    return json.dumps({
        'labels': (data['date']).to_list(),
        'data_deaths_new_dod': (data['deaths_new_dod']).to_list()
    })