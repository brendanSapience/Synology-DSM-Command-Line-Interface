import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import StdResponses
import AuthResponses
import logging

def get_login_url(dsmversion, login, password, sessionname):

    CgiModule=""
    UrlParameters=""
    Headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    if dsmversion=="7.0":
        CgiModule = "/webapi/auth.cgi?"
        params = { 'api' : 'SYNO.API.Auth', 'version' : '6', 'method' : 'login', 'account': login, 'passwd':password,'session':sessionname}
    else:
        return False,UrlParameters,Headers

    UrlParameters = CgiModule+urllib.parse.urlencode(params)
    return True,UrlParameters,Headers

def login(dsmversion,url,login,password,sessionname):

    IsVersionSupported,URLParams,headers = get_login_url(dsmversion,login,password,sessionname)
    if not IsVersionSupported:
        logging.debug("Unsupported DSM Version: {}".format(dsmversion))
        print("Unsupported DSM Version")
        exit(1)

    FULLURL = urllib.parse.urljoin(url,URLParams)

    response = requests.request("GET", FULLURL, data=None, headers=headers)
    isAPICallOK = StdResponses.processAPIResponse(response)
    if(not isAPICallOK):
        exit(99)
    else:
        isError,Code = AuthResponses.Process_Auth_Login_Response(response)
        if(not isError):
            DataUtils.StoreAuthToken(Code,sessionname)
            DataUtils.StoreUrl(url,sessionname)
            DataUtils.StoreDSMVersion(dsmversion,sessionname)
            print("Token Stored in session: "+sessionname)

def logout(sessionname):
    DataUtils.DeleteSessionFiles(sessionname)
    print("Session deleted: "+sessionname)

def listSessions():
    SessionList,IsError = DataUtils.listSessions()
    if(IsError):
        print("Error retrieving session list.")
    else:
        print(SessionList)
