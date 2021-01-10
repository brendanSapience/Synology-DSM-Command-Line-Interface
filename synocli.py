##############################################################
#
# Author: Bren Sapience
# Date: Jan 2021
# Scope:
#
#
##############################################################
#!/usr/bin/env python3

import argparse
import sys
sys.path.insert(1, './logics')
sys.path.insert(1, './libs')
import AuthLogics
import NetworkLogics
import DataUtils

DEFAULT_DSM_VERSION = "7.0"
SupportedDSMVersions = ["7.0"]

#####
# NETWORK Functions
#####

def network(args):
    if not args.SESSIONNAME:
        parser.error('no session name passed')
    NetworkLogics.get_network_info(args.SESSIONNAME)

#####
# AUTH Functions
#####

def login(args):
    if not args.LOGIN:
        parser.error('no login passed')
    if not args.PWD:
        parser.error('no password passed')
    if not args.URL:
        parser.error('no url passed')
    if not args.SESSIONNAME:
        args.SESSIONNAME = DataUtils.RandomSessionNameGenerator()
    AuthLogics.login(args.DSMVERSION,args.URL,args.LOGIN,args.PWD,args.SESSIONNAME)

def logout(args):
    if not args.SESSIONNAME:
        parser.error('no session name passed')
    AuthLogics.logout(args.SESSIONNAME)

def listsessions(args):
    AuthLogics.listSessions()

#####
# ALL Parsers
#####

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='0.0.1')
subparsers = parser.add_subparsers()

#####
# AUTH Parser
# Authentication commands
# auth <login,logout,list>
#####

auth_parser = subparsers.add_parser('auth')
auth_subparsers = auth_parser.add_subparsers()

# auth login
login_parser = auth_subparsers.add_parser('login')
login_parser.add_argument('-u','--user',type=str,default="", help='DSM Login', dest="LOGIN")
login_parser.add_argument('-p', '--pwd',type=str,default="", help='DSM Password', dest="PWD")
login_parser.add_argument('-r', '--url',type=str,default="", help='DSM URL',dest="URL")
login_parser.add_argument('-v', '--version',type=str,default=DEFAULT_DSM_VERSION, help='DSM Version',dest="DSMVERSION")
login_parser.add_argument('-s', '--session',type=str,default="", help='Session Name',dest="SESSIONNAME")
login_parser.set_defaults(func=login)

# auth logout
login_parser = auth_subparsers.add_parser('logout')
login_parser.add_argument('-s', '--session',type=str,default="", help='Session Name',dest="SESSIONNAME")
login_parser.set_defaults(func=logout)

# auth list
sesslist_parser = auth_subparsers.add_parser('list')
sesslist_parser.set_defaults(func=listsessions)

#####
# NETWORK Parser
# network <show>
#####

# Network cxommands
network_parser = subparsers.add_parser('network')
network_subparsers = network_parser.add_subparsers()

# network show
network_show_parser = network_subparsers.add_parser('show')
network_show_parser.add_argument('--session','-s',type=str,default="", help='Session Name',dest="SESSIONNAME")
network_show_parser.set_defaults(func=network)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
