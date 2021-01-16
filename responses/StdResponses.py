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
        result = json.loads(response.text)
        #print(result)
        if 'error' in result:
            JsonError = result['error']
            if 'code' in JsonError:
                APIErrorCode = JsonError['code']

                if APIErrorCode == 100:
                    print("Error: DSM Returned an unknown error.")
                    return False
                elif APIErrorCode == 101:
                    print("Error: Invalid parameter passed to DSM.")
                    return False
                elif APIErrorCode == 102:
                    print("Error: The requested API / Service is not installed or does not exist.")
                    return False
                elif APIErrorCode == 103:
                    print("Error: The requested API / Service Method is not installed or does not exist.")
                    return False
                elif APIErrorCode == 104:
                    print("Error: The requested API / Service does not support the version.")
                    return False
                elif APIErrorCode == 105:
                    print("Error: DSM returned a permission issue with the current user.")
                    return False
                elif APIErrorCode == 106:
                    print("Error: the current session has timed out.")
                    return False
                elif APIErrorCode == 107:
                    print("Error: currrent session interrupted due to duplicate login.")
                    return False
            else:
                print("Undetermined API Error: "+str(result))
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
