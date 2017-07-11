# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import json


data = []

req = requests.get('http://www.cwb.gov.tw/V7/observe/24real/Data/C0D56.htm')
soup = BeautifulSoup(req.text,  "lxml")

rows = soup.findAll('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

print(json.dumps(data))    

