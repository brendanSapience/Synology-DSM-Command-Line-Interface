import json
import pandas as pd

def GetDeviceListAsCsv(jsonResults):

    out_df = pd.DataFrame(columns=['id','name','description','countPrincipals','version','createdBy','createdOn','updatedBy','updatedOn'])

    ItemList = jsonResults['list']
    for item in ItemList:
        ID = item['id']
        NAME = item['name']
        DESC = item['description']
        COUNT = item['countPrincipals']
        VERSION = item['version']
        CREATEDBY = item['createdBy']
        CREATEDON = item['createdOn']
        UPDATEDBY = item['updatedBy']
        UPDATEDON = item['updatedOn']

        new_row = {'id':ID,'name':NAME,'description':DESC,'countPrincipals':COUNT,'version':VERSION,'createdBy':CREATEDBY,'createdOn':CREATEDON,'updatedBy':UPDATEDBY,'updatedOn':UPDATEDON}
        out_df = out_df.append(new_row, ignore_index=True)

    return out_df.to_csv(index=False)
