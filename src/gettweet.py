#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import json
import datetime, time, sys

from requests_oauthlib import OAuth1Session

import cleaning


targetID = 'ayako_17miss4'

def main():
    """
    main process
    """
    try:
        keysfile = open('keys.json') 
        keys = json.load(keysfile)
        oauth = create_oauth_session(keys)
        target_tweet(oauth)
    except Exception as e:
        print('%r' % e, flush=True)
    

def create_oauth_session(oauth_key_dict):
    """
    make session
    """
    
    oauth = OAuth1Session(
                oauth_key_dict['consumer_key'],
                oauth_key_dict['consumer_secret'],
                oauth_key_dict['access_token'],
                oauth_key_dict['access_token_secret']
                )
    return oauth

def target_tweet(oauth):
    """
    getting tweets from @ayako_17miss4
    """
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    screen_name = targetID
    tweets = []
    max_id = 928226737539842048 # 対象者の最新のツイートID
    while True:
        params = { 'screen_name': screen_name, 'count':200, 'max_id': max_id }
        res = oauth.get(url, params=params)
        if res.status_code == 200:
            raw_tweets = json.loads(res.text)
            this_id = int(raw_tweets[-1]['id'])
            print('tweet success', max_id, flush=True)
        else:
            print('tweet failed', max_id, flush=True)
            print(res, res.text)
            break
        if max_id == this_id:
            break
        max_id = this_id
        tweets += [ tweet['text'].replace('\n', '    ')  for tweet in raw_tweets if tweet['retweeted'] == False]
    print(tweets) 
    cleaning.main('\n'.join(tweets), 'target')

def my_tl(oauth):
    """
    getting tweets from my timeline
    """
    url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    tweets = []
    max_id = 927834468848508928 # 現在自分のTLにある最新のツイートIDを指定
    count = 0
    while True:
        params = { 'count': 200, 'max_id': max_id }
        res = oauth.get(url, params=params)
        if res.status_code == 200:
            raw_tweets = json.loads(res.text)
            this_id = int(raw_tweets[-1]['id'])
            print('tweet success', this_id, flush=True)
        else:
            print('tweet failed', max_id, flush=True)
            print(res, res.text)
            break
        if max_id == this_id:
            break
        if count == 18:
            break
        count += 1
        max_id = this_id
        tweets += [ tweet['text'].replace('\n', '    ')  for tweet in raw_tweets if tweet['retweeted'] == False]
        [print(tweet) for tweet in raw_tweets if tweet['retweeted'] == True]
    cleaning.main('\n'.join(tweets), 'other')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('%r' % e, flush=True)
