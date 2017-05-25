#!/usr/bin/env python
#!python3

import requests, bs4

res = requests.get('https://weather.com/weather/tenday/l/01879')
try:
	res.raise_for_status()
except Exception as e:
	print('Problem reaching site: %s' %(e))

weather_page = bs4.BeautifulSoup(res.text,"html.parser")

day_list = []
for day in weather_page.find_all("span", {"class" : "day-detail"}):
	day_list.append(day.getText())

#for i in day_list:
	#print(i)

temp_list = []
for block in weather_page.find_all("td", {"class" : "temp"}):
	for div in block:
		for span in div.find_all("span"):
			if span not in div.find_all("span", {"class" : "slash"}): 
				temp = list(span.getText())
				print(temp[0:1])

#for i in temp_list:
#	print(i)

precip_list = []
for precip in weather_page.find_all("td", {"class" : "precip"}):
	precip_list.append(precip.getText())

#for i in precip_list:
#	print(i)

weather_obj_list = []
for i in range(15):
	d = {
	'day' : day_list[i],
	#'high' : temp_list[i][0],
	#'low' : temp_list[i][1],
	'precip' : precip_list[i]
	}
	weather_obj_list.append(d)
for i in weather_obj_list:
	print(i)
