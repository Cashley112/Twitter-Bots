import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = "VwFRaINdfh7Ll9Odim6zWNYcx"
    consumer_secret = "2txel8Nh1e570c130J54h9TvVysovenNAkURnOigCVnFP19mcw"
    access_token = "881677256824934400-8rTTPd3whSO4MTA7boonCumM6ByojGB"
    access_token_secret = "eo2PljMxAKEqYLrq9q0VYFIIOBUoQIjBWsg2erscixIaw"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api