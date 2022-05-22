import logging
import pandas as pd
import json
import azure.functions as func


def main(req: func.HttpRequest) -> str:
    data = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/vaccination/vax_malaysia.csv')

    day = req.params.get('day')
    data = data.loc[data['date'].isin((data['date'].unique())[-30 if not day else -int(day):])]

    data = data.loc[:,['date','daily_partial', 'daily_full', 'daily_booster','daily']]
    return json.dumps({
        'labels': (data['date']).to_list(),
        'data_daily_partial': (data['daily_partial']).to_list(),
        'data_daily_full': (data['daily_full']).to_list(),
        'data_daily_booster': (data['daily_booster']).to_list(),
        'data_daily': (data['daily']).to_list()
    })