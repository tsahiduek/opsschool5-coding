from requests import get
import sys
import argparse

weather_access_key = "Insert_access_key"


def query_city_weather(city_name, unit_name):
    url_address = "http://api.weatherstack.com/current?access_key={access_key}".format(access_key=weather_access_key)
    request_url = get("{url}&query={query}&units={units}".format(url=url_address, query=city_name, units=unit_name))
    return request_url.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '-c')

    if len(sys.argv) < 2:
        print('''
SyntaxError: A minimum of one city is required to execute this script!
Try on of these:
* London
* Paris
* Berlin

Or open a case at : https://www.gov.il/he/Departments/Guides/police_public_complaints_unit
        ''')
        sys.exit()

    if str(sys.argv[-1]) == '-f':
        degree_type = "Fahrenheit"
        units_type = "f"
    else:
        degree_type = "Celsius"
        units_type = "m"

    city_for_query = str(sys.argv[1])
    city_list = city_for_query.split(",")
    for c in city_list:
        url_read = query_city_weather(city_name=c, unit_name=units_type)
        if "success" in url_read:
            print('''
ValidationError: The city chosen could not be found, please check if name is spelled correctly, or try on of these:
* London
* Paris
* Berlin
            ''')
            sys.exit()
        else:
            weather = url_read["current"]["temperature"]
            print(
                "The weather in {city} is {temperatue} {degree}".format(city=c, temperatue=weather, degree=degree_type))


if __name__ == "__main__":
    main()
