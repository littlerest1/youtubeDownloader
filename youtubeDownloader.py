#  fileName [link] [format] [quality] [subtitle]
# Chinese subtitle caption code = "zh-Hans" (simplify) caption = "zh-Hant" (traditional) caption = "zh" (without specify)
# Korean subtitle caption code = "ko"
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unicodedata
from bs4 import BeautifulSoup
import requests 
import urllib
from datetime import datetime,date
from urllib.request import urlopen
from pytube import *
import sys
import time
import os

#<div id="date" class="style-scope ytd-video-primary-info-renderer"><span id="dot" class="style-scope ytd-video-primary-info-renderer">•</span><yt-formatted-string class="style-scope ytd-video-primary-info-renderer">2017年12月2日</yt-formatted-string></div>
#<span class="view-count style-scope yt-view-count-renderer">977,770,033次观看</span>
#<yt-formatted-string class="style-scope ytd-video-primary-info-renderer">2018年6月4日</yt-formatted-string>
#<yt-formatted-string id="text" class="style-scope ytd-toggle-button-renderer style-default-active" aria-label="918,870 人顶过">91万</yt-formatted-string>

# creating function 
def scrape_info(url): 
	
	# getting the request from url 
	r = requests.get(url) 
	
	# converting the text 
	s = BeautifulSoup(r.text, "html.parser") 
	
    # finding meta info for title 
	title = s.find("span", class_="watch-title").text.replace("\n", "") 

    # finding publish date
	publish = s.find('strong', 'watch-time-text').get_text()
	publish = publish.replace("Published on ", "")

    # finding meta info for views 
	views = s.find("div", class_="watch-view-count").text 

	# finding meta info for likes 
	likes = s.find("span", class_="like-button-renderer").span.button.text 

	# saving this data in dictionary 
	data = {'title':title, 'views':views.replace(" views",""), 'likes':likes,'date':publish.replace("Premiered ","")} 
	
	# returning the dictionary 
	return data 
  
def compare_strs(s1, s2):
  str1 = ""
  str2 = ""
  for k in s1:
      str1 += str(ord(k))
  for k in s2:
      str2 += str(ord(k))
  return str1 in str2

if __name__ == "__main__": 
    # get the link from argument and use beautiful soup to extract video info
    link = sys.argv[1]
    data = scrape_info(link) 
    print("Video Information ")
    print("title:",data['title'])
    print("publish date:",data['date'])
    print("views",data['views'])
    print("likes:", data['likes'])

    # get the download requirement 
    quality = 'no'
    format = 'mp4'
    subtitle = False
    language = 'en'
    if len(sys.argv) > 2 and sys.argv[2] == 'mp3':
        format = 'mp3'

    if len(sys.argv) > 3:
        if sys.argv[3] != 'no':
            quality = sys.argv[3]
        if len(sys.argv) > 4:
            subtitle = True
            language = sys.argv[4]
    
    print("Downloading  ",link,quality,subtitle,format,language)
    yt = YouTube(link)
    title = yt.title
    print("title  ", title)
    #print(yt.captions.all()) # check the avaliable captions
    
    # download video clip by specific requirement
    if format == 'mp3':
        # filter the audio link and download audio only and change the file format in folder
        yt.streams.filter(only_audio=True)[0].download()
        files = os.listdir('.')
        files.sort(key=os.path.getctime,reverse=True)
        for f in files :
            if "." in f and f.split('.')[1] == 'mp4':
                os.rename(f,f.split('.')[0]+'.mp3')
                print("Converting to mp3")
                break
    
    # download video clip in mp4 format and if quliaty is not specify it will use the first link to download
    elif format == 'mp4' and quality != 'no':
        streams = yt.streams.first()
        streams.download()
    ''' 
     if subtitle caption download required download it in both srt and txt format so that I can checkout and change
     if I need to add some comments or addition
     caption file will use download time as file name for use e.g. dmy-hms
    '''
    if subtitle == True:
        today = date.today()
        # today's date in day month year e.g. 19052020
        current_date = today.strftime("%d%m%Y")
        now = datetime.now()
        # current time = date + current time in hour minutes second  e.g. filename = 19052020-194403
        current_time = current_date + '-' + now.strftime("%H%M%S")

        file1 = open(current_time+'.txt',"w+") 
        file2 = open(current_time+'.srt',"w+")
        caption = yt.captions.get_by_language_code(language) 
        str = caption.generate_srt_captions()
        print("Downloading caption",language)
        file2.write(str)
        file1.write(str)
        file1.close()
        file2.close()
        #print(caption.generate_srt_captions())

