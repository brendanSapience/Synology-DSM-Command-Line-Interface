import json
import pandas as pd
import logging
import sys

sys.path.insert(1, './libs')
import ConvUtils

def GetListAsCsv(jsonResults):

    ItemList = jsonResults['data']['files']
    AllRows = []
    for item in ItemList:

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


def GetShareListAsCsv(jsonResults):

    ItemList = jsonResults['data']['shares']
    AllRows = []
    for item in ItemList:

        details = item["additional"]["volume_status"]

        isDir = item["isdir"]
        fName = item["name"]
        fPath = item["path"]
        fFreeSpace = details['freespace']
        fTotalSpace = details['totalspace']

        new_row = {
        'name':fName,
        'isDir':isDir,
        'path':fPath,
        'totalSpace':ConvUtils.sizeof_fmt(fTotalSpace,"B"),
        'freeSpace':ConvUtils.sizeof_fmt(fFreeSpace,"B")
        }

        AllRows.append(new_row)

    myDFAdditional = pd.DataFrame(AllRows)

    return myDFAdditional
