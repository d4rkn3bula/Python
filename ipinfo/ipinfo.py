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

# ipinfo IP geolocation API function
def ipinfo_geolocation(g_ip):
	token = keyring.get_password("ipinfo", "username")
	base_url = "https://ipinfo.io/"
	uri = "?token="
	request = requests.get(base_url + g_ip + uri + token)
	data = json.loads(request.text)
	print(json.dumps(data, indent =4, sort_keys=True))

# ipinfo reverse IP API function
def ipinfo_reverseIP(r_ip):
	token = keyring.get_password("ipinfo", "username")
	base_url = "https://ipinfo.io/domains/"
	uri = "?token="
	request = requests.get(base_url + r_ip + uri + token)
	data = json.loads(request.text)
	print(json.dumps(data, indent =4, sort_keys=True))

# main function
def main():
	g_ip = sys.argv[1]
	ipinfo_geolocation(g_ip)
	r_ip = sys.argv[1]
	ipinfo_reverseIP(r_ip)


if __name__ == "__main__":
	main()
