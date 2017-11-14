import csv
from bs4 import BeautifulSoup
import numpy as np
import requests

page = requests.get('https://coinmarketcap.com')
soup = BeautifulSoup(page.content, 'html.parser')
tmp = soup.find('tr', id='id-bitcoin').get_text()
data = []
for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')
    data.append([tds[1].text.strip('\n').lower(), tds[3].text.strip('\n').lower()])
for i in range(len(data)):
    data[i][0] = data[i][0].replace('\n','')
    data[i][1] = data[i][1].replace('$','')

#print(data)

list = [['btcbitcoin'],['vtcvertcoin'], ['omgomisego']]
for i in range(len(data)):
    for x in range(len(list)):
        if data[i][0] in list[x]:
          list[x].append(data[i][1])

print(list)
 #tmp = tmp
#print(tmp)


#måde at gøre det på hvor den henter hver enkelt coin en ad gangen
#url = 'https://coinmarketcap.com/currencies/'
#list = ['bitcoin','vertcoin', 'omisego']

#for i in range(len(list)):
#    urltmp = url + list[i]
#    page = requests.get(urltmp)
#    soup = BeautifulSoup(page.content, 'html.parser')
#    tmp = soup.find('span', id = 'quote_price').get_text()
#    tmp = tmp[1:]
 #   print(tmp)