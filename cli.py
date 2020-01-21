import json
import urllib
import click


@click.command()
@click.option('--city', help='This will add City or Cities Location')
@click.option('--T', 'temperature', type=click.Choice(['Celsius', 'Fahrenheit']), default='Celsius', help='Temperature unit')
def weather_value(city, temperature):
    if temperature == "Fahrenheit":
        units_type = "f"
    else:
        units_type = "m"
    cities = city.split(',')

    for city in cities:
        city = urllib.parse.quote(str(city))
        url = ('http://api.weatherstack.com/current?access_key=65b235108b498590b8a76ada343e2bc6&query={}&units={}'.format(city,
                                                                                                  units_type))
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    try:
        dict_location = data['location']
        dict_location_city = dict_location.get('name', {})
        dict_temperature = (data['current']).get('temperature', {})
        print('The weather in ' + dict_location_city() + ' is' + ' ' + str(dict_temperature) + ' ' + temperature)
    except:
        print("ERROR: The city does not exists, Please try different one as Dublin, Moscow")


if __name__ == '__main__':
    weather_value()