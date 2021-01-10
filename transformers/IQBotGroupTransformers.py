import json
import pandas as pd

def GetGroupListAsCsv(jsonResults):

    out_df = pd.DataFrame(columns=['id','name','orgId','LIID','LIName','GroupID','GroupName','environment','status',
    'running','lastModifiedByUser','lastModifiedTimestamp','description'])

    ItemList = jsonResults['data']
    for item in ItemList:
        a1 = item['id']
        a2 = item['name']
        a3 = item['organizationId']
        a4 = item['projectId']
        a5 = item['projectName']
        a6 = item['categoryId']
        a7 = item['categoryName']
        a8 = item['environment']
        a9 = item['status']
        b1 = item['running']
        b2 = item['lastModifiedByUser']
        b3 = item['lastModifiedTimestamp']
        b4 = item['description']
        # = item['']
        # = item['']
        # = item['']
        # = item['']
        # = item['']

        new_row = {
            'id':a1,'name':a2,'orgId':a3,'LIID':a4,'LIName':a5,'GroupID':a6,'GroupName':a7,'environment':a8,'status':a9,
            'running':b1,'lastModifiedByUser':b2,'lastModifiedTimestamp':b3,'description':b4
        }
        out_df = out_df.append(new_row, ignore_index=True)

    return out_df.to_csv(index=False)
