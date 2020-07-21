# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 09:19:10 2020

@author: Johnny Tsai
"""

import requests
from bs4 import BeautifulSoup

url = 'https://car.watch.impress.co.jp/category/tyre/'

headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4122.7 Mobile Safari/537.36'}

response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')

head_news = []
head_link = []

for i in range(5):
    news = soup.select('.title')[i+1].text
    head_news.append(news)
    link = soup.select('.title a')[i].get('href')
    head_link.append(link)

def lineNotifyMessage(token, msg):
   headers = {
       "Authorization": "Bearer " + token, 
   }
	
   payload = {'message': msg}
   r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
   return r.status_code
	
message0 = '\n' + head_news[0] + '\n' + head_link[0]
message1 = '\n' + head_news[1] + '\n' + head_link[1]
message2 = '\n' + head_news[2] + '\n' + head_link[2]
message3 = '\n' + head_news[3] + '\n' + head_link[3]
message4 = '\n' + head_news[4] + '\n' + head_link[4]
           
token = 'o83VHkmfBS0k6HWakuOcyEXbBsy4YUoqUwyoJzo26vL'

lineNotifyMessage(token, message0)
lineNotifyMessage(token, message1)
lineNotifyMessage(token, message2)
lineNotifyMessage(token, message3)
lineNotifyMessage(token, message4)
