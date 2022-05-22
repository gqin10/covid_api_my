import logging
import pandas as pd
import json
import azure.functions as func


def main(req: func.HttpRequest) -> str:
    data = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/deaths_malaysia.csv')
    day = req.params.get('day')

    data = data.loc[data['date'].isin((data['date'].unique())[-30 if not day else -int(day):])]

    return json.dumps({
        'labels': (data['date']).to_list(),
        'data_deaths_new_dod': (data['deaths_new_dod']).to_list()
    })