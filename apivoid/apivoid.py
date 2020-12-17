#!/usr/bin/python3

'''
Python script to query IPv4 reputation utilizing apivoid.com
'''

# imported modules
import requests
import json
import keyring
import re
import argparse

# argparse function
# setup multiple arguments to call different apivoid functions

def get_args():

    parser = argparse.ArgumentParser(prog='apivoid lookup script', description='returns IPv4 reputation of the provided IP')
    parser.add_argument('-i', '--ipaddress', help='Input IPv4 address to run the IP reputation function')
    parser.add_argument('-d', '--domain', help='Input domain to run the domain blacklist function')
    parser.add_argument('-u', '--url', help='Input URL to run the URL reputation function')
    parser.add_argument('-n', '--dns', help='Input domain to run the DNS record function')

    args = parser.parse_args()

    return args

# check for valid IP address, supply error message, kill process
def is_ip(ip):

    ip_re = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
    if ip_re.match(ip):
        return ip
    else:
        print("process killed")
        print(f"{ip} is not an ip address")
        exit()

# ip reputation function
def ip_reputation(ip_rep):

    token = keyring.get_password("apivoid", "username")
    base_url = "https://endpoint.apivoid.com/iprep/v1/pay-as-you-go/?key="
    request = requests.get(base_url + token + "&ip=" + ip_rep)
    data = json.loads(request.text)
    print(json.dumps(data, indent=4, sort_keys=True))

# main
def main():

    args = get_args()
    ip_rep = args.ipaddress

    if args.ipaddress:
        is_ip(ip_rep)
        ip_reputation(ip_rep)
    else:
        print('Something went wrong')


if __name__ == "__main__":
    main()
