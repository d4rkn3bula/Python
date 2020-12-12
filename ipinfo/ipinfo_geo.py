#!/usr/bin/python3

# python script utilizing ipinfo's API
# prints json blob data to terminal

import requests
import json
import keyring
import sys

# ipinfo IP geolocation API function
def ipinfo_geolocation():
	token = keyring.get_password("ipinfo", "username")
	base_url = "https://ipinfo.io/"
	uri = "?token="
	g_ip = sys.argv[1]

	r = requests.get(base_url + g_ip + uri + token)
	data = json.loads(r.text)
	print(json.dumps(data, indent =4, sort_keys=True))

# ipinfo reverse IP API function
def ipinfo_reverseIP():
	token = keyring.get_password("ipinfo", "username")
	base_url = "https://ipinfo.io/domains/"
	uri = "?token="
	r_ip = sys.argv[1]

	r = requests.get(base_url + r_ip + uri + token)
	data = json.loads(r.text)
	print(json.dumps(data, indent =4, sort_keys=True))


def main():
	ipinfo_geolocation()
	ipinfo_reverseIP()


if __name__ == "__main__":
	main()
