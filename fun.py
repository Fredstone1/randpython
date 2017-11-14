import csv
from bs4 import BeautifulSoup
import numpy as np
import requests
import time
start_time = time.time()

my_list = []
data = []
pfval = []
class crypto():

    def updatePF(self):
        print(data)
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
                if data[i][0] in my_list[x]:
                    my_list[x].append(data[i][1])
        self.updatecsv('crypto.csv',my_list)
        del data[:]
        return my_list and data

    def updatecsv(self, csvfile, datalist):
        with open(csvfile, 'w') as cf:
            wr = csv.writer(cf, delimiter=',')
            for line in datalist:
                wr.writerow([line])
            cf.close()

    def seecsv(self, csvfile):
        with open(csvfile, newline='') as cf:
            cfreader = csv.reader(cf, delimiter=' ')
            for row in cfreader:
                print(''.join(row))
            cf.close()


    def addcoin(self, coinname):
        my_list.append([coinname])
        return my_list


f = crypto()
f.addcoin('btcbitcoin')
f.addcoin('vtcvertcoin')
f.updatePF()
time.sleep(200)
f.updatePF()
print('\n ')
print(my_list)
print("--- %s seconds ---" % (time.time() - start_time))


