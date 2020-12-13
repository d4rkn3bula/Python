# ipinfo.py

ipinfo.py is a simple script that will allow you to specify an IPv4 address and retrieve geolocation or perform a reverse IP lookup.

## Installation

```bash
python3 -m pip install -r requirements.txt
```

## Usage

```python
usage: ipinfo lookup script [-h] [-g GEOLOCATE] [-r REVERSEIP]

returns information of a given ip address

optional arguments:
  -h, --help            show this help message and exit
  -g GEOLOCATE, --geolocate GEOLOCATE
                        Input IPv4 address to run the geolocation function
  -r REVERSEIP, --reverseip REVERSEIP
                        Input IPv4 address to run the reverse ip check function

examples:
python3 ipinfo.py -g 1.1.1.1
python3 ipinfo.py -r 1.1.1.1
```
