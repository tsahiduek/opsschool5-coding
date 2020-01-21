#!/usr/bin/env python
from requests import get
import sys
import argparse


parser = argparse.ArgumentParser(description="adding City Location")
parser.add_argument('city_location', help="This will add City Location")
parser.add_argument('-f', '-c', help="This will convert Temperature from Celsius to Fahrenheit")
# parser.add_argument('-d', '--database', nargs='+')
arguments = parser.parse_args()


weather = get('http://api.weatherstack.com/current?access_key=65b235108b498590b8a76ada343e2bc6&query=' + arguments.city_location)
data = weather.json()
try:
    city_location = data['request']['query']
    temperature_value = data['current']['temperature']
    if str(sys.argv[-1]) == '-f':
        temp_scale = "Fahrenheit"
        units_type = "f"
    else:
        temp_scale = "Celsius"
        units_type = "m"
    print('The weather in ' + str(city_location) + ' is' + ' ' + str(temperature_value) + ' ' + temp_scale)
except:
    print('ERROR: The city does not exists, Please try different one as Dublin, Moscow or Israel')