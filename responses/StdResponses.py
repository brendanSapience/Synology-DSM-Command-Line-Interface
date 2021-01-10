import requests
import json
import sys
import os

def ProcessBool(myBool):
    if(str(type(myBool)) == "<class 'str'>"):
        if(myBool in ['True','true','t','yes']):
            return True
        if(myBool in ['False','false','f','no']):
            return False
    else:
        return myBool

def isAnomalousHtmlResponse(text):
    if("<html" in text and "</html>" in text):
        return True
    else:
        return False

def processAPIResponse(response):
    if(response.status_code != 200):
        logging.debug("DSM API Error: {}".format(response.status_code))
        print("API Error Code: "+str(response.status_code))
        return False
    else:
        return True

def ProcessStdResponse(res,CsvOutput):
    CsvOutput = ProcessBool(CsvOutput)
    if isAnomalousHtmlResponse(res.text):
        print("Error: You need to log back in.")
        exit(1)
    if(res.status_code >= 400):

        print("Error Code: "+str(res.status_code))
        try:
            result = json.loads(res.text)
            if result['message']:
                print("Error Message: "+result['details'])
                return True,None
        except:
            return True,None

        return True,None

    else:
        try:
            return False,CsvOutput
        except:
            print("Unknown Error.")
            return True,None
