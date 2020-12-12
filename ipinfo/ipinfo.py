#!/usr/bin/python3

'''
python script utilizing ipinfo's API and prints json blob data to terminal
ipinfo reference:  https://ipinfo.io
You must setup keyring first "python3 -m pip install keyring"
Keyring reference: https://pypi.org/project/keyring/
>>> import keyring
>>> keyring.set_password("system", "username", "password")
>>> keyring.get_password("system", "username")
'password'
'''

import requests
import json
import keyring
import sys
import re


# check ip using regex, kill process if not
def is_ip(ip):
	ip_re = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
	if ip_re.match(ip):
		return ip
	else:
		print("process killed")
		print(f"{ip} is not an ip address")
		exit()

# ipinfo IP geolocation API function
def ipinfo_geolocation(ip):
	token = keyring.get_password("ipinfo", "username")
	base_url = "https://ipinfo.io/"
	uri = "?token="
	request = requests.get(base_url + ip + uri + token)
	data = json.loads(request.text)
	print(json.dumps(data, indent =4, sort_keys=True))

# ipinfo reverse IP API function
def ipinfo_reverseIP(ip):
	token = keyring.get_password("ipinfo", "username")
	base_url = "https://ipinfo.io/domains/"
	uri = "?token="
	request = requests.get(base_url + ip + uri + token)
	data = json.loads(request.text)
	print(json.dumps(data, indent =4, sort_keys=True))


# main function
def main():
	ip = sys.argv[1]
	is_ip(ip)
	ipinfo_geolocation(ip)
	ipinfo_reverseIP(ip)


if __name__ == "__main__":
	main()
