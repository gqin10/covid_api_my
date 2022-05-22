import logging
import pandas as pd
import json
import azure.functions as func


def main(req: func.HttpRequest) -> str:
    data = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/vaccination/vax_malaysia.csv')

    day = req.params.get('day')
    data = data.loc[data['date'].isin((data['date'].unique())[-1 if not day else -int(day):])]

    data = data.loc[:,['date','cumul_partial', 'cumul_full', 'cumul_booster','cumul']]
    return json.dumps({
        'labels': (data['date']).to_list(),
        'data_cumul_partial': (data['cumul_partial']).to_list(),
        'data_cumul_full': (data['cumul_full']).to_list(),
        'data_cumul_booster': (data['cumul_booster']).to_list(),
        'data_cumul': (data['cumul']).to_list()
    })