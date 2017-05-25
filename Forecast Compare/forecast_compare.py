#!/usr/bin/env python
#!python3

import requests, bs4

res = requests.get('https://weather.com/weather/tenday/l/01879')
res.raise_for_status()

weather_page = bs4.BeautifulSoup(res.text,"html.parser")

day_list = []
for day in weather_page.find_all("span", {"class" : "day-detail"}):
	day_list.append(day.getText())

temp_list = []
for temp in weather_page.find_all("td", {"class" : "temp"}):
	temp = list[temp.getText()]
	temp_list.append([temp[0:1],temp[4:5]])

precip_list = []
for precip in weather_page.find_all("td", {"class" : "precip"}):
	precip_list.append(precip.getText())

weather_obj_list = []
for i in range(15):
	d = {
	  'day' : day_list[i],
	  'high' : temp_list[i][0],
      'low' : temp_list[i][1],
	  'precip' : precip_list[i]
	}
	weather_obj_list.append(d)

for i in weather_obj_list:
	print(i)
