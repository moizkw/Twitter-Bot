import tweepy
from Yahoo import gainers, losers, most_active, earnings_date, world_indices

def main():
    # Authenticate to Twitter (CONFIDENTIAL Information)
    consumer_key = 'XXX' 
    consumer_secret = 'XXX' 
    access_token = 'XXX' 
    access_token_secret = 'XXX' 
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Verifying Credentials
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    # Creating Tweets
    tweet = "Top Gainers:\n"+gainers()+"\n#finance #money #investing #stocks #crypto #wealth #trading #wallstreet #invest #success #entrepreneur"
    if len(tweet) < 280:
        print(len(tweet))
        api.update_status(tweet)
    else:
        print('Tweet is too long',len(tweet))

    tweet = "Top Losers:\n"+losers()+"\n#finance #money #investing #stocks #crypto #wealth #trading #wallstreet #invest #success"
    if len(tweet) < 280:
        print(len(tweet))
        api.update_status(tweet)
    else:
        print('Tweet is too long',len(tweet))

    tweet = "Most Active:\n"+most_active()+"\n#finance #money #investing #stocks #crypto #wealth #trading #wallstreet #invest #success #entrepreneur"
    if len(tweet) < 280:
        print(len(tweet))
        api.update_status(tweet)
    else:
        print('Tweet is too long',len(tweet))

if __name__ == "__main__":
    main()
