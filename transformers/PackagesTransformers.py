import json
import pandas as pd
import logging


def GetListAsCsv(jsonResults):
    out_df = pd.DataFrame(columns=['name','id','status','version','autoupdate','beta','updated'])

    ItemList = jsonResults['data']['packages']
    for item in ItemList:

        a1 = item['id']
        a2 = item['name']
        a3 = item['version']
        a4 = item['additional']['autoupdate']
        a5 = item['additional']['beta']
        a6 = item['additional']['status']
        a7 = item['additional']['updated_at']

        new_row = {'name':a2,'id':a1,'status':a6,'version':a3,'autoupdate':a4,'beta':a5,'updated':a7}

        out_df = out_df.append(new_row, ignore_index=True)

    return out_df#out_df.to_csv(index=False)
