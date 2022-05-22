import logging
import pandas as pd
import azure.functions as func
import json


def main(req: func.HttpRequest) -> str:
    data = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/icu.csv')
    day = req.params.get('day')
    state = req.params.get('state')

    date = (data['date'].unique())[-1 if not day else -int(day):]
    data = data[data['date'].isin(date)]

    if state != None:
        data = data[data['state'] == state]
        return json.dumps({
            'labels': (data['date']).to_list(),
            'data_beds_icu_total': (data['beds_icu_total']).to_list(),
            'data_beds_icu_covid': (data['beds_icu_covid']).to_list()
    })
    else:
        return json.dumps({
            'labels': (data['state']).to_list(),
            'data_beds_icu_total': (data['beds_icu_total']).to_list(),
            'data_beds_icu_covid': (data['beds_icu_covid']).to_list()
        })


    