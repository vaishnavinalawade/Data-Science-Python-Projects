import tweepy
import time

# NOTE: flush=True is just for running this script

CONSUMER_KEY = '####'
CONSUMER_SECRET = '####'
ACCESS_KEY = '####'
ACCESS_SECRET = '####'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_id.txt'

def retrive_last_id(file_name):
    f_read = open(file_name, 'r')
    last_id = int(f_read.read().strip())
    f_read.close()
    return last_id

def store_last_id(last_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_id))
    f_write.close()
    return

def reply_tweet():
    print('This is a bot for replying to Tweets!!!!')
    
    last_id = retrive_last_id(FILE_NAME)
    mentions = api.mentions_timeline(last_id, tweet_mode = 'extended')
    
    for mention in reversed(mentions):
        print(str(mention.id)+' '+mention.text, flush=True)
        last_id = mention.id
        store_last_id(last_id, FILE_NAME)
        
        if 'helloword' or 'hello' or 'hi' in mention.text.lower():
            print('Found Greetings... Replying back', flush=True)
            api.update_status('@'+mention.user.screen_name+' '+"Hello back to you!!!", mention.id)
        
        elif 'bye' or 'good bye' in mention.text.lower():
            print('Found Bye.... Replying back', flush=True)
            api.update_status('@'+mention.user.screen_name+' '+"Good Bye!!!", mention.id)
        
        else:
            print('Generic message.... Replying back', flush=True)
            api.update_status('@'+mention.user.screen_name+' '+"Will get back to you later", mention.id)

while True:
    reply_tweet()
    time.sleep(10)
