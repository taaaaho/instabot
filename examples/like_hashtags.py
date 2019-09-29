# coding: UTF-8
"""
    instabot example

    Workflow:
        Like last images with hashtag.
"""

import argparse
import os
import sys
from time import sleep

# import line_notify

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
# parser.add_argument('hashtags', type=str, nargs='+', help='hashtags')
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)

tags =  ["いいねした人で気になった人フォロー","いいねした人全員フォローする","いいね返します","likeforlike","いいね返し","portrait","写真好きな人と繋がりたい","ファインダー越>しの私の世界"]
wait = 25 * 60  # in seconds => 25 minutes
retry = 5 * 60 * 60 # in hours => 5 hours

while True:
    try:
        for hashtag in tags:
            # line_notify.notify('Start Like:{0}'.format(hashtag)) 
            bot.like_hashtag(hashtag)
            # line_notify.notify('Like:{0} Bot will sleep:{1} seconds'.format(str(bot.total['likes']), str(wait))) 
            sleep(wait)
    except Exception as e:
        # line_notify.notify('Instabot Exception:'+ str(e))
        sleep(retry)
