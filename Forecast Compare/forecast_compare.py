#!/usr/bin/env python
#!python3

import requests, bs4, shelve, datetime, os

#compare attributes of weather objects of the same date to count differences
def diff_exist(obj_1, obj_2):
	diff = 0

	if obj_1['day'] != obj2['day']:
		return diff
	if obj_1['high'] != obj_2['high']:
		diff += 1
	if obj_1['precip'] != obj_2['precip']:
		diff += 1
	if obj_1['low'] != obj_2['low']:
		diff += 1
	
	return diff
		

res = requests.get('https://weather.com/weather/tenday/l/01879')
print("Status code: %s" %(res.status_code))
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
			#extract temperature data surrounding slash-mark on website
			if span not in div.find_all("span", {"class" : "slash"}): 
				temp = list(span.getText())
				first_num = str(temp[0])
				second_num = str(temp[1])
				temp_list.append(first_num+second_num)

#separate highs (odd indices) from lows (even indices) in temp_list
low_list = []
high_list = []
index = 0;
for i in temp_list:
	index += 1
	if index % 2 == 0:
		low_list.append(i)
	else:
		high_list.append(i)

#print("Lows:")
#for i in low_list:
#	print(i)

#print("Highs:")
#for i in high_list:
#	print(i)

precip_list = []
for precip in weather_page.find_all("td", {"class" : "precip"}):
	precip_list.append(precip.getText())

#for i in precip_list:
#	print(i)

#construct list of weather objects
#each weather object contains day, low, high, precip
#list containts current day + next 14 days
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

#get date format for storage of weather_obj_list
today = datetime.datetime.now()
year = str(today.year)
day = str(today.day)
date = year + '-' + day

#compare current weather object with past weather objects saved to shelve file
differences = 0
if os.path.exists('Weather_Data'):
	weather_data_shelf = shelve.open('Weather_Data')
	for shelve_obj_list in weather_data_shelf:
		for shelve_obj in weather_data_shelf[shelve_obj_list]:
			for current_obj in weather_obj_list:
				if shelve_obj['day'] == current_obj['day']:
					differences += diff_exist(shelve_obj, current_obj)

	#store current weather_obj_list in shelf file with yyyy-dd name
	weather_data_shelf[date] = weather_obj_list

	#store differences calculated via diff_exist
	weather_data_shelf['differences'] += differences
	print("Found %s differences so far." %(differences))
	weather_data_shelf.close()
else:
	#create shelve file if not found
	print("No Previous Weather Data Found...\n Writing New Weather Data File")
	weather_data_shelf = shelve.open('Weather_Data')
	weather_data_shelf[date] = weather_obj_list
	weather_data_shelf['differences'] = 0
	weather_data_shelf.close()


