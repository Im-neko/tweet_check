#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re

import pandas as pd
from lxml import html

def clean_tweet(text):
    """
    一旦全てを置換し、文末の改行コードだけ元に戻す。
    この際、置換するワードは今までの自分の記憶を辿り、
    今までつぶやいたことがないワードが望ましい
    """
    data = text.split('\n')
    # 正規表現でIDとURL,ハッシュタグ、RTを消す
    replypattern = '@[\w]+'
    hashpattern = '#[\w]+'
    rtpattern = 'RT : +'
    urlpattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'
    whitelist = ['Twitter for iPhone', 'TweetDeck']
    processedtweets = []
    
    for i, tweet in enumerate(data):
        text = re.sub(replypattern, '', tweet)
        text = re.sub(hashpattern, '', text)
        text = re.sub(rtpattern, '', text)
        text = re.sub(urlpattern, '', text)
        if isinstance(text, str) and not text.split():
            pass
        else:
            processedtweets.append(text)
    return processedtweets
    
def main(text, name):
    newDF = clean_tweet(text)
    with open('./../ml_data/'+name+'.txt', 'a') as f:
        f.write('\n'.join(newDF))

if __name__=='__main__':
    main()
