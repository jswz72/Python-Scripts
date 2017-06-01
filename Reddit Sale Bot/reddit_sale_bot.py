#!/usr/bin/env python
#!python3

import praw, time, re, shelve, os, smtplib

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

user_agent = "web:com.example.myredditapp:v1.2.3 (by /u/" + "buildapcsalesb0t" + ")"
r = praw.Reddit(user_agent = user_agent, client_id = "", client_secret = "", username = "", password = "")

print('\nLogging in...')
#r.login()   #put in username and password in ext file

subreddit = r.subreddit("")
print('\nLoading subreddit...\n')

if os.path.exists('Previous_Deals'):
	previous_deals_shelf = shelve.open('Previous_Deals')	
	cache = previous_deals_shelf['cache']
else:
	previous_deals_shelf = shelve.open('Previous_Deals')	
	cache = []

bot_email = ''
bot_email_password = ''
recipient_email = ''

smtpObj = smtplib.SMTP('',587)
smtpObj.starttls()
smtpObj.login(bot_email, bot_email_password)
email_count = 0

for submission in subreddit.new(limit = 10):
        if "[]" in submission.title:
                #regex to find all dollar amounts < $100
                double_digit_regex = re.compile(r'(\$( )?\d(\d)?\.(\d)?(\d)?)')
                double_digits = double_digit_regex.search(submission.title)
                #regex to find all dollar amounts < upper limit
                upper_limit_regex = re.compile(r'(\$1[0-5]\d(.)?\d\d)')
                upper_limits = upper_limit_regex.search(submission.title)
                if str(type(double_digits)) != "<type 'NoneType'>" or str(type(upper_limits)) != "<type 'NoneType'>":
                        if submission.title not in cache:
                                smtpObj.sendmail(bot_email, recipient_email, 'Subject: ' + str(subreddit) + ' deal\n' + submission.title)
                                print('email success')
				email_count += 1
                                cache.append(submission.title)
if email_count == 0:
	print('No new deals found')
smtpObj.quit()
previous_deals_shelf['cache'] = cache
previous_deals_shelf.close()

