import tweepy


CONSUMER_KEY = 'YOUR CONSUMER_KEY'
CONSUMER_SECRET = 'Your CONSUMER_SECRET_KEY'

ACESS_KEY = 'YOUR ACESS_KEY'
ACESS_SECRET = 'YOUR ACESS SECRET_KEY'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACESS_KEY,ACESS_SECRET)


api = tweepy.API(auth,wait_on_rate_limit=True)



def like_my_boss_pub():

    for pub in api.user_timeline(screen_name='YOUR PERSONNAL ACCOUNT SCREEN NAME',count=200):
        try:
            api.create_favorite(pub.id)
            print("Liking "+ str(pub.id))

        #The exception will be triggered when all posts have been liked.
        except:
            return

def retweet_my_boss_pub():
    for pub in api.user_timeline(screen_name='YOUR PERSONNAL ACCOUNT SCREEN NAME',count=200):
        try:
            api.retweet(pub.id)
            print("retweet "+ str(pub.id))

        #The exception will be triggered when all posts have been retweeted.
        except:
            return


def follow_back_my_followers():
    
    for follower in tweepy.Cursor(api.followers).items():

        if follower.id not in api.friends_ids(): #check if the follower is not already my friend
            follower.follow()
            print("following "+follower.screen_name)
        else:
            return

def retweet_messi_is_the_best():

    i= 0

    for tweet in api.home_timeline(count=1000):
        
        if 'messi' in tweet.text.lower():

            try:
                api.retweet(tweet.id)
                print('retweet '+tweet.author)
            except:
                pass
        i+=1

        if i == 10**6:
            return


while True:

    
    like_my_boss_pub()
    retweet_my_boss_pub()
    
    #check if all follower is already followed
    if set(api.followers_ids()) - set(api.friends_ids()) != set():
        follow_back_my_followers()

    retweet_messi_is_the_best()