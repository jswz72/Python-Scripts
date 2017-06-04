#!/usr/bin/env python
#!python3

import praw, time, re, shelve, os, smtplib

print("Enter reddit bot username")
bot_name = raw_input()

print("Enter reddit bot password")
bot_password = raw_input()

print("Enter client_id")
bot_id = raw_input()

print("Enter secret")
bot_secret = raw_input()

print("Enter intended subreddit")
deal_subreddit = raw_input()

print("Enter keyword to search for")
keyword = raw_input()

print("Enter price upper-limit")
price_limit = raw_input()

print("Enter rate to fetch posts (1-100)")
rate_limit = raw_input()

bot_agent = "web:com.example.myredditapp:v1.2.3 (by /u/" + bot_name + ")"
r = praw.Reddit(user_agent = bot_agent, client_id = bot_id, client_secret = bot_secret, username = bot_name, password = bot_password)

print('\nLogging in...')

subreddit = r.subreddit(deal_subreddit)
print('\nLoading subreddit...\n')

#Check to see if Previous Deals shelffile exists
if os.path.exists('Previous_Deals'):
	previous_deals_shelf = shelve.open('Previous_Deals')	
	cache = previous_deals_shelf['cache']
else:
	previous_deals_shelf = shelve.open('Previous_Deals')	
	cache = []

print('Enter bot (sender) email')
bot_email = raw_input()

print('Enter bot (sender) email password')
bot_email_password = raw_input()

print('Enter recipient email')
recipient_email = raw_input()

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.starttls()
smtpObj.login(bot_email, bot_email_password)
email_count = 0

for submission in subreddit.new(limit = 10):
        if keyword in submission.title:
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

