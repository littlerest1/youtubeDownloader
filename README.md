# youtubeDownloader
Youtube downloader include mp3/mp4 quality specify and subtitle caption download
# Usage:
#  python3 youtubeDownloader.py [link] [format] [quality] [subtitle]
link = youtube link
format = mp3/mp4
quality = no (for mp3 format)/1080p/720p ...
subtitle caption language  = en(default)/ zh (chinese if exist) / ko (korean if exist)
if you don't need to download subtitle leave this argument empty
# Requirements
python3
pytube:
https://pypi.org/project/pytube/
https://python-pytube.readthedocs.io/en/latest/
urllib
# Future features
Video information: # of views/likes/dislikes, publish date
