import csv
from bs4 import BeautifulSoup
import numpy as np
import requests
import time
start_time = time.time()
my_list = []
with open('crypto.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    my_list = your_list
timeList = ['time']
with open('time.csv', 'r') as t:
    reader = csv.reader(t)
    tmplist = list(reader)
    timeList = tmplist
data = []
pfval = []
class crypto():
    def updatePF(self):
        tid = time.strftime('%c')
        page = requests.get('https://coinmarketcap.com')
        soup = BeautifulSoup(page.content, 'html.parser')

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
                    break
        timeList.append([tid])
        self.updatecsv('crypto.csv',my_list)
        self.updatecsv('time.csv',timeList)
        del data[:]

        return my_list and data

    def updatecsv(self, csvfile, datalist):
        with open(csvfile, 'w') as cf:
            wr = csv.writer(cf, delimiter=',', lineterminator='\n')
            for line in datalist:
                wr.writerow(line)
            cf.close()

    def seecsv(self, csvfile):
        with open(csvfile, newline='') as cf:
            cfreader = csv.reader(cf, delimiter=' ')
            for row in cfreader:
                print(''.join(row))
            cf.close()

    def addcoin(self, coinname):
        for x in range(len(my_list)):
            if coinname in my_list[x]:
                break
        else:
            my_list.append([coinname])
        return my_list
    #def createGraph(self, csvfile):


f = crypto()
f.addcoin('btcbitcoin')
f.addcoin('vtcvertcoin')
f.updatePF()
print('\n ')

print(my_list)

print(timeList)

print("------ %s seconds ------" % (time.time() - start_time))


