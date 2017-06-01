#!/usr/bin/env python
#!python3

import praw, time, random, re, shelve

#print("Enter reddit username")
#username = raw_input()

#print("Enter reddit password")
#password = raw_input()

#print("Enter client_id")
#client_id = raw_input()

#print("Enter secret")
#secret = raw_input()

#print("Enter desired subreddit")
#subreddit = raw_input()

#print("Enter keyword to search for")
#keyword = raw_input()

#print("Enter price upper-limit")
#price_limit = raw_input()

user_agent = ""
r = praw.Reddit(user_agent = user_agent, client_id = "", client_secret = "OQynvMsuD-", username = "", password = "")

print('\nLogging in...')
#r.login()   #put in username and password in ext file

subreddit = r.subreddit("")
print('\nLoading subreddit...\n')

if os.path.exists('Previous_Deals'):
	previous_deals_shelf = shelve.open('Previous_Deals')
	cache = previous_deals_shelf[cache]
else:
	cache = []

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.starttls()
smtpObj.login( bot_email, bot_email_password)

for submission in subreddit.new(limit = "10"):
	if keyword in submission.title:
		#regex to find all dollar amounts < $100
		double_digit_regex = re.compile(r'(\$( )?\d(\d)?\.(\d)?(\d)?)')
		double_digits = double_digit_regex.search(submission.title)
		#regex to find all dollar amounts < upper limit
		upper_limit_regex = re.compile(r'(\$1[0-5]\d(.)?\d\d)')
		upper_limits = upper_limit_regex.search(submission.title)
		if str(type(double_digits)) != "<type 'NoneType'>" or str(type(upper_limits)) != "<type 'NoneType'>":
			if submission.title not in cache:
				smtpObj.sendmail(bot_email, recipient_email, 'Subject: ' + subreddit + ' deal\n' + submission.title)
				print(submission.title)
				cache.append(submission.title)
smtpObj.quit()
