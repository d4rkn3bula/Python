#!/usr/bin/python3
# simple script to pass a text file with a list of base64 strings to decode
# imported modules
import sys, os, base64
# function for command line argument to specify a file
# example: python base64_decode.py encodedData.txt
def inputfile():
	filepath = sys.argv[1]
	if not os.path.isfile(filepath):
		print("File path {} does not exist. Exiting...".format(filepath))
		sys.exit()

# function for reading specified file and returning to a list
def file():
	filepath = sys.argv[1]
	with open(filepath) as fp:
		fp = fp.readlines()
		return fp

# function for base64 decoding the list contents while creating a new txt file to write to 
def base64decode(file):
	with open("b64output.txt", 'w') as b64output:
		for line in file:
			b64data = base64.b64decode(line).rstrip().decode('utf-8')
			b64output.write(b64data)
			b64output.write("\n")
			print(b64data)

# main function
def main():
	inputfile()
	b64List = file()
	base64decode(b64List)

if __name__ == "__main__":
	main()