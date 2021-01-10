import requests
import json
import sys
import os

sys.path.insert(1, './libs')
import DataUtils
import StdResponses


def Process_Auth_Login_Response(res):
    if(res.status_code==200):
        try:
            result = json.loads(res.text)
            if 'error' in result:
                DSMAPIRetCode = result['error']['code']
                #print("Code: "+str(DSMAPIRetCode))
                return True,DSMAPIRetCode

            if 'data' in result:
                SID = result['data']['sid']
                #print(SID)
                return False,SID
        except:
            #print("Unknown Error.")
            return True,""
