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

portfolio = []
with open('portfolio.csv', 'r') as f:
    reader = csv.reader(f)
    pflist = list(reader)
    portfolio = pflist

data = []
pfval = []
PFsum = 0


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
                    my_list[x].append(tid)
                    break
        self.updatecsv('crypto.csv', my_list)
        del data[:]
        return my_list and data and tid

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

    def addcoin(self, coinname, amount):
        for x in range(len(my_list)):
            if coinname in my_list[x]:
                break
        else:
            my_list.append([coinname])
        for x in range(len(portfolio)):
            if coinname in portfolio[x]:
                break
        else:
            portfolio.append([coinname, amount])

        self.updatecsv('portfolio.csv', portfolio)
        return my_list and portfolio

    def calcPFVal(self):
        tid = time.strftime('%c')
        self.updatePF()
        PFsum = 0
        for x in range(len(portfolio) - 1):
            for i in range(len(my_list)):
                if portfolio[x][0] in my_list[x]:
                    tmp1 = float(my_list[x][len(my_list[x]) - 2])
                    tmp2 = float((portfolio[x][1]))
                    PFsum = PFsum + tmp1 * tmp2
                if 'hej' in portfolio[x]:
                    portfolio.remove(portfolio[x])
        PFsum = str(round(PFsum, 2)) + ' $'
        portfolio.append([PFsum, tid, 'hej'])
        self.updatecsv('portfolio.csv', portfolio)
        return PFsum

        # def createGraph(self, csvfile):


f = crypto()
f.addcoin('vtcvertcoin', 17.812)
f.addcoin('omgomisego', 2.4975)
f.addcoin('xrpripple', 40)
f.addcoin('neoneo', 0.48749)
f.addcoin('arkark', 5.9975)
f.addcoin('xlmstellar lumens', 234.535)
f.updatePF()
print('\n ')
print(f.calcPFVal())
# print(timeList)


print("------ %s seconds ------" % (time.time() - start_time))
