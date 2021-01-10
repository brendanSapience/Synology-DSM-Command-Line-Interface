import argparse
import sys

# Authentication commands
# auth <login,logout>
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

# auth logout
sesslist_parser = auth_subparsers.add_parser('list')
sesslist_parser.set_defaults(func=listsessions)
