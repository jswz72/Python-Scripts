import praw, time, random

r = praw.Reddit(user_agent = "", client_id = "", client_secret = "", username = "", password="")
print('\nLoggin in...')
#r.login()   #put in username and password in ext file

cache = []  #holds comments already replied to
tries = [0,0]
response = []
    
def run_bot():
    subreddit = r.subreddit("pics")
    print('\nLoading subreddits...')
    comments = subreddit.comments(limit=1) 

    print('Grabbing comments...')
    for comment in comments:
        comment_text = comment.body.lower()
        if comment.id not in cache:
            try:
                words = comment_text.split()
                for i in words:
                    response.append(random.choice(words))
                comment.reply(' '.join(response))
                print('Responded: \n' + ' '.join(response))
                cache.append(comment.id)
            except:
                print("\nNot avaiable:")
                #print(comment_text)
                tries[0] += 1
                tries[1] += 10
                #print(tries)
        return tries
                
            

while True:
    tries = run_bot()
    print(str(tries[0]) + ' tries since successful post')
    print(str(tries[1]) + ' seconds since successful post')
    response = []
    time.sleep(10)
