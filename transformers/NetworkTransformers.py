import json
import pandas as pd
import logging


def GetListAsCsv(jsonResults):

    myDF = pd.DataFrame(jsonResults['data'])
    if 'pass' in myDF:
        myDF.pop('pass')
    return myDF
