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
    anonymity = (data["data"]["report"]["anonymity"])
    blacklists = (data["data"]["report"]["blacklists"])
    information = (data["data"]["report"]["information"])
    del (data["data"]["report"]["blacklists"]["engines"])

    print("Anonymity:")
    for key, value in anonymity.items():
        print(key, ":", value)
    print("\n")

    print("Blacklists:")
    for key, value in blacklists.items():
        print(key, ":", value)
    print("\n")

    print("Information:")
    for key, value in information.items():
        print(key, ":", value)


# domain reputation function

def d_reputation(d_rep):

    token = keyring.get_password("apivoid", "username")
    base_url = "https://endpoint.apivoid.com/domainbl/v1/pay-as-you-go/?key="
    request = requests.get(base_url + token + "&host=" + d_rep)
    data = json.loads(request.text)
    report = (data["data"]["report"])
    blacklists = (data["data"]["report"]['blacklists'])
    category = (data["data"]["report"]["category"])
    server = (data["data"]["report"]["server"])
    del (data["data"]["report"]["blacklists"]["engines"])
    del (data["data"]["report"]["blacklists"])
    del (data["data"]["report"]["category"])
    del (data["data"]["report"]["server"])

    print("Report:")
    for key, value in report.items():
        print(key, ":", value)
    print("\n")

    print("Blacklists:")
    for key, value in blacklists.items():
        print(key, ":", value)
    print("\n")

    print("Category:")
    for key, value in category.items():
        print(key, ":", value)
    print("\n")

    print("Server:")
    for key, value in server.items():
        print(key, ":", value)

# url reputation function
# main
def main():

    args = get_args()
    ip_rep = args.ipaddress
    d_rep = args.domain
    u_rep = args.url
    n_rep = args.dns

    if args.ipaddress:
        is_ip(ip_rep)
        ip_reputation(ip_rep)
    elif args.domain:
        d_reputation(d_rep)
    else:
        print('Something went wrong')


if __name__ == "__main__":
    main()
