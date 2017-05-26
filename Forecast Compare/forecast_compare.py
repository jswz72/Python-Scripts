#!/usr/bin/env python
#!python3

import requests, bs4, shelve, datetime

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
				first_num = str(temp[0])
				second_num = str(temp[1])
				temp_list.append(first_num+second_num)

#separate highs from lows in temp_list
low_list = []
high_list = []
index = 0;
for i in temp_list:
	index += 1
	if index % 2 == 0:
		low_list.append(i)
	else:
		high_list.append(i)

precip_list = []
for precip in weather_page.find_all("td", {"class" : "precip"}):
	precip_list.append(precip.getText())

#for i in precip_list:
#	print(i)

#construct list of weather objects
#each weather object contains day, low, high, precip
#list containts current day + next 15 days
weather_obj_list = []
for i in range(15):
	d = {
	'day' : day_list[i],
	'low' : low_list[i],
	'high' : high_list[i],
	'precip' : precip_list[i]
	}
	weather_obj_list.append(d)

#for i in weather_obj_list:
#	print(i)

#get date format for storage
today = datetime.datetime.now()
year = str(today.year)
day = str(today.day)
date = year + '-' + day

#store list of weather objects in shelf file 
weather_data_shelf = shelv.open('weather_data')
weather_data_shelf['date'] = weather_obj_list
