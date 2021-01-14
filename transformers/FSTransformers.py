import json
import pandas as pd
import logging
import sys

sys.path.insert(1, './libs')
import ConvUtils

def GetListAsCsv(jsonResults):

    #myDF = pd.DataFrame(jsonResults['data']["task"])
    #myDF.pop('additional')
    #print(myDF)

    ItemList = jsonResults['data']['files']
    AllRows = []
    for item in ItemList:

        #print(item["additional"]["detail"])
        details = item["additional"]

        isDir = item["isdir"]
        fName = item["name"]
        fPath = item["path"]
        fSize = details['size']
        fRealPath = details['real_path']

        new_row = {
        'name':fName,
        'isDir':isDir,
        'path':fPath,
        'size':ConvUtils.sizeof_fmt(fSize,"B"),
        'realPath':fRealPath,
        'path':fPath
        }
        
        AllRows.append(new_row)

    myDFAdditional = pd.DataFrame(AllRows)

    return myDFAdditional
