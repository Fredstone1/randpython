import csv
from bs4 import BeautifulSoup
import numpy as np
import requests
import time
start_time = time.time()

my_list = []
data = []
pfval = []
def updatePF():
    print(data)
    print(my_list)
    page = requests.get('https://coinmarketcap.com')
    soup = BeautifulSoup(page.content, 'html.parser')
    tmp = soup.find('tr', id='id-bitcoin').get_text()
    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        data.append([tds[1].text.strip('\n').lower(), tds[3].text.strip('\n').lower()])
    for i in range(len(data)):
        data[i][0] = data[i][0].replace('\n', '')
        data[i][1] = data[i][1].replace('$', '')
    for i in range(len(data)):
        for x in range(len(my_list)):
            if data[i][0] in my_list[x] and data[i][1] not in my_list[x]:
                my_list[x].append(data[i][1])
    updatecsv('crypto.csv',my_list)

def updatecsv(csvfile, datalist):
    with open(csvfile, 'w') as cf:
        wr = csv.writer(cf, delimiter=',')
        for line in datalist:
            wr.writerow([line])
        cf.close()

def seecsv(csvfile):
    with open(csvfile, newline='') as cf:
        cfreader = csv.reader(cf, delimiter=' ')
        for row in cfreader:
            print(''.join(row))
        cf.close()

#def portfolio():

#def calcPFVal():

def addcoin(coinname):
    my_list.append([coinname])

addcoin('btcbitcoin')
addcoin('vtcvertcoin')
updatePF()
time.sleep(240)
updatePF()

print('\n ')
print(my_list)
print("--- %s seconds ---" % (time.time() - start_time))


