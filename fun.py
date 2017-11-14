import csv
from bs4 import BeautifulSoup
import numpy as np
list = []
class crypto:
    def updatecsv(csvfile, data):
        with open(csvfile, 'w') as cf:
            wr = csv.writer(cf, delimiter=',')
            for line in data:
                wr.writerow([line])
            cf.close()

    def seecsv(csvfile):
        with open(csvfile, newline='') as cf:
            cfreader = csv.reader(cf, delimiter=' ')
            for row in cfreader:
                print(''.join(row))
            cf.close()

    #def portfolio():
    def addcoin(coinname):
        list.append([coinname])



    #coin1 = ['vtcvertcoin']
    #coin1.append(5.3)
    #coin2 = ['btcbitcoin']
    #data = [coin1, coin2]
    #updatecsv('crypto.csv', data)
    #seecsv('crypto.csv')


