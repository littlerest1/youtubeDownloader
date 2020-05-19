# youtubeDownloader <br/>
Youtube downloader include mp3/mp4 quality specify and subtitle caption download
# Usage: <br/>
python3 youtubeDownloader.py [link] [format] [quality] [subtitle] <br/>
link = youtube link <br/>
*if you just want to check the information of the video please leave below arguments empty <br/>
format = mp3/mp4 <br/>
quality = no (for mp3 format)/1080p/720p ... <br/>
subtitle caption language  = en(default)/ zh (chinese if exist) / ko (korean if exist) <br/>
*if you don't need to download subtitle leave this argument empty <br/>
# Requirements <br/>
python3 <br/>
pytube <br/>
https://pypi.org/project/pytube/ <br/>
https://python-pytube.readthedocs.io/en/latest/ <br/>
beautifulsoup <br/>
https://www.crummy.com/software/BeautifulSoup/bs4/doc/ <br/>
https://pypi.org/project/beautifulsoup4/ <br/>
urllib <br/>
# Sample Output <br/>
input : python3 youtubeDownloader.py https://www.youtube.com/watch?v=ALj5MKjy2BU mp3 no ko </br>
*download fire-bts mv in mp3 format includes Korean lyrics subtitle caption </br>
output: </br>
Video Information </br>
title:     [MV] BTS(방탄소년단) _ FIRE (불타오르네) </br>
publish date: May 1, 2016 </br>
views 650,276,473 </br>
likes: 6,879,061 </br>
Downloading   https://www.youtube.com/watch?v=ALj5MKjy2BU no True mp3 ko </br>
title   [MV] BTS(방탄소년단) _ FIRE (불타오르네) </br>
Converting to mp3 </br>
Downloading caption ko
