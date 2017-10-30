import csv
import bs4
import numpy as np

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

    def portfolio():


    coin1 = ['vtc', 4.8, 5.1]
    coin1.append(5.3)
    coin2 = ['btc', 5900, 6100, 6200]
    data = [coin1, coin2]
    updatecsv('crypto.csv', data)
    seecsv('crypto.csv')
