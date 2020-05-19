#  fileName [link] [format] [quality] [subtitle]
# Chinese subtitle caption code = "zh-Hans" (simplify) caption = "zh-Hant" (traditional) caption = "zh" (without specify)
# Korean subtitle caption code = "ko"
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unicodedata
from bs4 import BeautifulSoup
import urllib
from datetime import datetime
from urllib.request import urlopen
from pytube import *
import sys
import time
import os

#<div id="date" class="style-scope ytd-video-primary-info-renderer"><span id="dot" class="style-scope ytd-video-primary-info-renderer">•</span><yt-formatted-string class="style-scope ytd-video-primary-info-renderer">2017年12月2日</yt-formatted-string></div>
#<span class="view-count style-scope yt-view-count-renderer">977,770,033次观看</span>
#<yt-formatted-string class="style-scope ytd-video-primary-info-renderer">2018年6月4日</yt-formatted-string>
#<yt-formatted-string id="text" class="style-scope ytd-toggle-button-renderer style-default-active" aria-label="918,870 人顶过">91万</yt-formatted-string>
def Video_info(url):
    html = urlopen(url).read().decode('utf-8')   
    
    soup = BeautifulSoup(html, "html.parser")
    date = soup.find('div', {'id' : 'info-text'})
    d = str(date)
    print(d)

'''
    spans = soup.find('span', {'class' : 'view-count'})
    inf = str(spans)
    count = inf.split('>')[1]
    countV = count.split('<')[0]
    print(countV)
'''
    
  
       

def compare_strs(s1, s2):
  str1 = ""
  str2 = ""
  for k in s1:
      str1 += str(ord(k))
  for k in s2:
      str2 += str(ord(k))
  return str1 in str2


link = sys.argv[1]
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
print("Video Information ")
#print(yt.captions.all())
#Video_info(link)

if format == 'mp3':
       # print(yt.streams.filter(only_audio=True))
   # t = yt.streams.filter(only_audio=True).first()
   # print(yt.streams.all())
   # print(yt.streams.filter(only_audio=True)[0])
    yt.streams.filter(only_audio=True)[0].download()
    files = os.listdir('.')
    files.sort(key=os.path.getctime,reverse=True)
    for f in files :
       print(f)
       if "." in f and f.split('.')[1] == 'mp4':
          os.rename(f,f.split('.')[0]+'.mp3')
          print("Converting to mp3")
          break
   # tempT = os.getcwd() + '/' + yt.title + '.mp3'
    #os.rename(title,tempT)
elif format == 'mp4' and quality != 'no':
    streams = yt.streams.first()
    streams.download()
if subtitle == True:
    now = datetime.now()
    current_time = now.strftime("%H%M%S")

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

