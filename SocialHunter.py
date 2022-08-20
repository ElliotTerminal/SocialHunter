# -*- coding: UTF-8 -*-
# ToolName   : SocialHunter
# Author     : ElliotTerminal
# License    : GPL V3
# Copyright  : ElliotTerminal (2022-2023)
# Github     : https://github.com/ElliotTerminal
# Description: SocialHunter - OSINT Tool to Hunt-Down Usernames
# Language   : Python
# If you copy open source code, please consider giving credit

'''imports'''
import requests
import time

username = input('\033[92m{>} Enter username to HUNT: ')

# Instagram
instagram = f'https://www.instagram.com/{username}'

# Facebook
facebook = f'https://www.facebook.com/{username}'

#Twitter
twitter = f'https://www.twitter.com/{username}'

# Youtube
youtube = f'https://www.youtube.com/{username}'

# Blogger
blogger = f'https://{username}.blogspot.com'

# Google+
google_plus = f'https://plus.google.com/s/{username}/top'

# Reddit
reddit = f'https://www.reddit.com/user/{username}'

# Wordpress
wordpress = f'https://{username}.wordpress.com'

# Pinterest
pinterest = f'https://www.pinterest.com/{username}'

# Github
github = f'https://www.github.com/{username}'

# Tumblr
tumblr = f'https://{username}.tumblr.com'

# Flickr
flickr = f'https://www.flickr.com/people/{username}'

# Steam
steam = f'https://steamcommunity.com/id/{username}'

# Vimeo
vimeo = f'https://vimeo.com/{username}'

# Soundcloud
soundcloud = f'https://soundcloud.com/{username}'

# Disqus
disqus = f'https://disqus.com/by/{username}'

# Medium
medium = f'https://medium.com/@{username}'

# Deviantart
deviantart = f'https://{username}.deviantart.com'

# Vk
vk = f'https://vk.com/{username}'

# About.Me
aboutme = f'https://about.me/{username}'

# Imgur
imgur = f'https://imgur.com/user/{username}'

# Flipboard
flipboard = f'https://flipboard.com/@{username}'

# Slideshare
slideshare = f'https://slideshare.net/{username}'

# Fotolog
fotolog = f'https://fotolog.com/{username}'

# Spotify
spotify = f'https://open.spotify.com/user/{username}'

# Mixcloud
mixcloud = f'https://www.mixcloud.com/{username}'

# Scribd
scribd = f'https://www.scribd.com/{username}'

# Badoo
badoo = f'https://www.badoo.com/en/{username}'

# Patreon
patreon = f'https://www.patreon.com/{username}'

# Bitbucket
bitbucket = f'https://bitbucket.org/{username}'

# Dailymotion
dailymotion = f'https://www.dailymotion.com/{username}'

# Etsy
etsy = f'https://www.etsy.com/shop/{username}'

# Cashme
cashme = f'https://cash.me/{username}'

# Behance
behance = f'https://www.behance.net/{username}'

# Goodreads
goodreads = f'https://www.goodreads.com/{username}'

# Instructables
instructables = f'https://www.instructables.com/member/{username}'

# Keybase
keybase = f'https://keybase.io/{username}'

# Kongregate
kongregate = f'https://kongregate.com/accounts/{username}'

# Livejournal
livejournal = f'https://{username}.livejournal.com'

# Angellist
angellist = f'https://angel.co/{username}'

# Last.Fm
last_fm = f'https://last.fm/user/{username}'

# Dribble
dribbble = f'https://dribbble.com/{username}'

# Codecademy
codecademy = f'https://www.codecademy.com/{username}'

# Gravatar
gravatar = f'https://en.gravatar.com/{username}'

# Pastebin
pastebin = f'https://pastebin.com/u/{username}'

# Foursquare
foursquare = f'https://foursquare.com/{username}'

# Robolox
roblox = f'https://www.roblox.com/user.aspx?username={username}'

# Gumroad
gumroad = f'https://www.gumroad.com/{username}'

# Newsground
newsground = f'https://{username}.newgrounds.com'

# Wattpad
wattpad = f'https://www.wattpad.com/user/{username}'

# Canva
canva = f'https://www.canva.com/{username}'

# Creativemarket
creative_market = f'https://creativemarket.com/{username}'

# Trakt
trakt = f'https://www.trakt.tv/users/{username}'

# 500px
five_hundred_px = f'https://500px.com/{username}'

# Buzzfeed
buzzfeed = f'https://buzzfeed.com/{username}'

# Tripadvisor
tripadvisor = f'https://tripadvisor.com/members/{username}'

# Hubpages
hubpages = f'https://{username}.hubpages.com'

# Contently
contently = f'https://{username}.contently.com'

# Houzz
houzz = f'https://houzz.com/user/{username}'

#Blip.Fm
blipfm = f'https://blip.fm/{username}'

# Wikipedia
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

# Hackernews
hackernews = f'https://news.ycombinator.com/user?id={username}'

# Codementor
codementor = f'https://www.codementor.io/{username}'

# Reverbnation
reverb_nation = f'https://www.reverbnation.com/{username}'

# Designspiration
designspiration = f'https://www.designspiration.net/{username}'

# Bandcamp
bandcamp = f'https://www.bandcamp.com/{username}'

# COLOURLOVERS
colourlovers = f'https://www.colourlovers.com/love/{username}'

# Ifttt
ifttt = f'https://www.ifttt.com/p/{username}'

# Ebay
ebay = f'https://www.ebay.com/usr/{username}'

# Slack
slack = f'https://{username}.slack.com'

# Okcupid
okcupid = f'https://www.okcupid.com/profile/{username}'

# Trip
trip = f'https://www.trip.skyscanner.com/user/{username}'

# Ello
ello = f'https://ello.co/{username}'

# Tracky
tracky = f'https://tracky.com/user/~{username}'

# Basecamp
basecamp = f'https://{username}.basecamphq.com/login'


''' Website List - Using It For Searching Of Username '''
WEBSITES = [
instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
]

''' Function For Color Printing '''
def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function

''' Printing The Colors '''
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')


''' Highlight '''
def banner():
    YELLOW(r'''
 .d8888.  .d88b.   .o88b. d888888b  .d8b.  db      db   db db    db d8b   db d888888b d88888b d8888b. 
 88'  YP .8P  Y8. d8P  Y8   `88'   d8' `8b 88      88   88 88    88 888o  88 `~~88~~' 88'     88  `8D 
 `8bo.   88    88 8P         88    88ooo88 88      88ooo88 88    88 88V8o 88    88    88ooooo 88oobY' 
   `Y8b. 88    88 8b         88    88~~~88 88      88~~~88 88    88 88 V8o88    88    88~~~~~ 88`8b   
 db   8D `8b  d8' Y8b  d8   .88.   88   88 88booo. 88   88 88b  d88 88  V888    88    88.     88 `88. 
 `8888Y'  `Y88P'   `Y88P' Y888888P YP   YP Y88888P YP   YP ~Y8888P' VP   V8P    YP    Y88888P 88   YD 
               
                                                                                        By - ElliotTerminal
  ''')

def search():
    GREEN(f'[>] Searching for username:{username}')
    time.sleep(0.5)
    print('started..')
    time.sleep(0.5)
    print('started..\n')
    time.sleep(0.5)

    GREEN(f'[>] SocialHunter is working\n')
    time.sleep(0.5)
    print('fetching..')
    time.sleep(0.5)
    print('fetching..\n')
    time.sleep(0.5)

    time.sleep(1)

    count = 0
    match = True
    for url in WEBSITES:
        r = requests.get(url)

        if r.status_code == 200:
            if match == True:
                GREEN('[>] FOUND MATCHES')
                match = False
            YELLOW(f'\n{url} - {r.status_code} - OK')
            if username in r.text:
                GREEN(f'POSITIVE MATCH: Username:{username} - text has been detected in url.')
            else:
                GREEN(f'POSITIVE MATCH: Username:{username} - \033[91mtext has NOT been detected in url, could be a FALSE POSITIVE.')
        count += 1
    
    total = len(WEBSITES)
    GREEN(f'FINISHED: A total of {count} MATCHES has been found out of {total} websites.')



if __name__=='__main__':
    banner()
    search()
