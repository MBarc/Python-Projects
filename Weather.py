'''
Author: Michael Barcelo
Github: MBarc

Background info: 

This script uses the OpenWeatherAPI.

The API's information is updated every 10 minutes. 

In order to use this script, you must have an API key provided by Open Weather.
'''

import requests

#URL to request weather information
api_address = "http://api.openweathermap.org/data/2.5/weather?"

#Put your API key here as a String
api_key = "appid=a0f3d0e12b1a25cb94e35c64d584e337"

#This is how the URL requests for the city.
small_url = "&q="

#Prompts the user for input
print("Please enter the city's name that you would like to check the weather of: ")
city = input("City Name: ")

#Forms the complete URL to request information from.
url = api_address + api_key + small_url + city
#print(url)

#Raw JSON data
json_data = requests.get(url).json()

#Fromatted JSON data = current weather
formatted_data = json_data['weather'][0]['main']

#Prints out the current weather of the city of the User's choosing
print(formatted_data)


