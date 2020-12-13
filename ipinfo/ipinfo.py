#!/usr/bin/python3

'''
Author: Kris Rostkowski
python script utilizing ipinfo's API and prints json blob data to terminal
ipinfo reference:  https://ipinfo.io
to install requirements, python3 -m pip install -r requirements.txt
'''

import requests
import json
import keyring
import re
import argparse

# argparse function
def get_args():

	parser = argparse.ArgumentParser(prog='ipinfo lookup script', description='returns information of a given ip address')
	parser.add_argument('-g', '--geolocate', help='Input IPv4 address to run the geolocation function')
	parser.add_argument('-r', '--reverseip', help='Input IPv4 address to run the reverse ip check function')

	args = parser.parse_args()

	return args

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
def ipinfo_geolocation(geo_ip):

	token = keyring.get_password("ipinfo", "username")
	base_url = "https://ipinfo.io/"
	uri = "?token="
	request = requests.get(base_url + geo_ip + uri + token)
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

	args = get_args()
	geo_ip = args.geolocate
	r_ip = args.reverseip

	if args.geolocate:
		is_ip(geo_ip)
		ipinfo_geolocation(geo_ip)
	elif args.reverseip:
		is_ip(r_ip)
		ipinfo_reverseIP(r_ip)
	# debugging
	else:
		print("Script is not functioning properly.")


if __name__ == "__main__":
	main()
