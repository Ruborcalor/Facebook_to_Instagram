#!/usr/bin/env python3

from facepy import GraphAPI
import json
import urllib.request
import requests
from InstagramAPI import InstagramAPI
from wand.image import Image
from wand.color import Color
import math

import hidden_info
#from abstraction import getLatestMediaID, hashtag

import time
from datetime import datetime, timedelta


""" Global Variables """

#script_start_time = datetime.utcnow()
script_start_time = datetime.utcnow() - timedelta(minutes=5)
uploaded_ids = []
toUpload_posts = []

""" Cole Test Account """
#username = hidden_info.coleUsername
#password = hidden_info.ploughPassword

""" Plough and Stars account """
username = hidden_info.ploughUsername
password = hidden_info.ploughPassword


""" Helper Functions """
def getLatestMediaID(usernameID=None):
	print("Getting latest media for user %s..." % usernameID)

	if usernameID:
		res = InstagramAPI.getUserFeed(usernameID)
	else:
		res = InstagramAPI.getSelfUserFeed()
	
	if res is True:
		feed = InstagramAPI.LastJson
		if (len(feed["items"])) > 0:
			latestMediaItem = feed["items"][0] # 0 indicates first item
			latestMediaItemID = latestMediaItem["caption"]["media_id"]
			print("%s's latest media ID is %s" % (username, latestMediaItemID)) 
			
			return latestMediaItemID
		else:
			print("No items found in users feed")
	else:
		print("Failed to get latest media from user's feed")


hashtag = """WhooooOoop!   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀



#Boston #bostonmusic #bostonmusicscene#bostonma #wednightbluesjam #bostonian #igboston#bostonnightlife #bostonbars #bostonbands#visitboston #cambma #localboston #bostonlocal#bostonfood #bostonbound #bostoneats#cambridgema #bandsofinstagram #bostonfoodie#livemusic #localmusic #supportlocal #eaterboston #bostonrestaurants
"""



InstagramAPI = InstagramAPI(username, password)


# Initialize the Graph API with a valid access token (optional,
# but will allow you to do all sorts of fun stuff).
oauth_access_token = hidden_info.oauth_access_token
graph = GraphAPI(oauth_access_token)





def trigger_upload(photo_info):
    #photo_info = (graph.get('me/posts?fields=message,full_picture,created_time,id'))['data'][0]

    pic_url = photo_info['full_picture']
    pic_caption = photo_info['message']
    pic_id = photo_info['id']

    photo_path = "toUpload"
    urllib.request.urlretrieve(pic_url, photo_path)

    with Image(filename=photo_path) as img:
        image_size = str(img.size)
        aspects = str(image_size[image_size.find("(") + 1: image_size.find(")")]).split(",")
        aspects = [float(aspect) for aspect in aspects]
        aspect_ratio = (aspects[0]) / (aspects[1])

        if aspect_ratio < 0.8:
            w_bor = int(math.ceil(aspects[1] * 0.8) - aspects[0])
            img.border(color=Color('transparent'), width=w_bor, height=0)
            img.save(filename=photo_path)

        if aspect_ratio > 1.91:
            h_bor = int((math.ceil(aspects[0] / 1.91) - aspects[1]) / 2)
            img.border(color=Color('transparent'), width=0, height=h_bor)
            img.save(filename=photo_path)



    InstagramAPI.login()  # login
    """Login to Instagram via API"""


    print(photo_path)
    print(pic_caption)
    InstagramAPI.uploadPhoto(photo_path, caption=pic_caption)

    latestMediaID = getLatestMediaID(usernameID = InstagramAPI.username_id)
    InstagramAPI.comment(latestMediaID, hashtag)

    uploaded_ids.append(pic_id)

while True:
    photo_feed = (graph.get('me/posts?fields=message,full_picture,created_time,id'))['data']
    #print(photo_feed)

    for post in photo_feed:
        created_time = datetime.strptime(post["created_time"][0: -5] + " UTC", "%Y-%m-%dT%H:%M:%S %Z")
        post_id = post['id']
        if (created_time > script_start_time and not post_id in uploaded_ids):
            toUpload_posts.append(post)

    print("Posts to Upload: ")
    print(toUpload_posts)

    for post in toUpload_posts:
        """ Uploading to Instagram """
        trigger_upload(post)

        """ Test Without Uploading to Instagram """
        #uploaded_ids.append(post['id'])

    print("Uploaded Ids: ")
    print(uploaded_ids)
    toUpload_posts = []


    time.sleep(10)
