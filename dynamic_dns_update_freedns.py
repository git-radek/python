#!/usr/bin/python3
# 2022/09/24 Radoslaw Michon.
# Dynamic DNS update script for freedns.42.pl
# Over time, many libs are deprecated e.g. xmlrpclib. Therefore, I changed the older python2 script to be compatible
# with the modern approach (python3 + xmlrpc). I hope someone will enjoy it!

import xmlrpc.client, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", help="username")
parser.add_argument("-p", "--password", help="password")
parser.add_argument("-z", "--zone", help="zone")
parser.add_argument("-r", "--recordname", help="recordname")
parser.add_argument("-o", "--oldaddress", help="old IP address - can be skipped if you are inserting/updating a record. Can be wildcard '*'.", default="*")
parser.add_argument("-n", "--newaddress", help="new IP address - can be skipped if you are deleting a record. Can be \"<dynamic>\", server will use IP you're connecting from.", default="<dynamic>")
parser.add_argument("-t", "--ttl", help="time to live <default: 600>", type=int, default=600)
parser.add_argument("-rev", "--updatereverse", help="update reverse DNS <1|0>", type=int, default=0)
parser.add_argument("-s", "--server", help="xmlrpc server URL <default: https://freedns.42.pl/xmlrpc.php>", default="https://freedns.42.pl/xmlrpc.php")
args = parser.parse_args()

params = \
{       "user"          : args.user,
        "password"      : args.password,
        "zone"          : args.zone,
        "name"          : args.recordname,
        "oldaddress"    : args.oldaddress,
        "newaddress"    : args.newaddress,
        "ttl"           : args.ttl,
        "updatereverse" : args.updatereverse,
}

def main():
    with xmlrpc.client.ServerProxy(args.server) as proxy:
        try:
            print(params)
            proxy.xname.updateArecord(params)
        except xmlrpc.client.Fault as e:
            print(e)
            exit(1)

if __name__ == "__main__":
    main()
