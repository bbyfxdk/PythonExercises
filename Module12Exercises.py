import json
import requests

# Exercise 1:
Request = "https://api.chucknorris.io/jokes/random"
Response = requests.get(Request).json()
print("Random Chuck Norris joke:")
print(Response["value"])

# Exercise 2:
City = input("Enter city: ")
City = City.capitalize()
Key = "################################"
Request = "https://api.openweathermap.org/data/2.5/weather?q=" + City + "&appid=" + Key + "&units=metric"
Response = requests.get(Request).json()
Weather = Response["Weather"][0]["Description"]
Temp = Response["Main"]["Temp"]
print(f"Current weather at {City}: {Weather}\nTemperature: {Temp}")