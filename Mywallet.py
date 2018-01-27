#!/usr/bin/env python
# This program buys some Dogecoins and sells them for a bigger price
#from bittrex import bittrex
import smtplib
from bittrex.bittrex import *
from email.mime.text import MIMEText


#server = smtplib.SMTP('internal-mail-router.oraclecorp.com',25) #port 465 or 587

api = Bittrex('6d0a3e7dbf11459db218928c8ea240c4', '69249e8eea454959b652e1822834432c')



def getbalanceof(currency):
    myBalance = api.get_balance(currency)
    x = myBalance["result"]
    price = x['Available']
    y = api.get_marketsummary('{0}-{1}'.format('USDT', currency))
    res = y["result"]
    lastprice = res[0]['Last']
    

    total = price * lastprice
    

    return total
#r = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=BTC-ADA")

#data = r.json()
#res = data["result"]

#print(res)
# Market to trade at
trade = 'USDT'
currency = 'ETH'
market = '{0}-{1}'.format(trade, currency)
# Amount of coins to buy
amount = 100
# How big of a profit you want to make
multiplier = 1.1

# Getting the BTC price for DOGE
#adasummary = api.get_marketsummary(market)
#res = adasummary["result"]
#dogeprice = res[0]['Last']
#print 'The price for {0} is {1:.8f} {2}.'.format(currency, dogeprice, trade)

#currency = 'ETH'
#Gets my ADA balance
#adabalance = api.get_balance(currency)
#res1 = adabalance["result"]
#print res1

allb= api.get_balances()
fsdaf =  allb["result"]
#resw = fsdaf[0]['Available']

#print (resw)
total = 0
for i in range(0,fsdaf.__len__()):
    f = fsdaf[i]['Available']
    if f != 0.0 and fsdaf[i]['Currency'] != 'USDT' and fsdaf[i]['Currency'] != 'XLM':
        t = getbalanceof(fsdaf[i]['Currency'])
        total += t
        print '{0}  = {1}$  '.format(fsdaf[i]['Currency'] , t )
print 'total in dollar = {0}'.format(total)    
strTotal = 'total in dollar = {0}'.format(total) 

#if total > 3500 or total < 3000:
#    server.sendmail("ami.meidar@oracle.com", "ami.meidar@oracle.com", strTotal)
#    server.quit()

    




#getbalanceof(api ,currency)
#x = float(adab)
#y = float(dogeprice)
#TotalinDollar= float(res) * float(dogeprice)
#print (TotalinDollar)
#api.buy_limit(market, amount, dogeprice)

#Buying 100 DOGE for BTC
###print 'Buying {0} {1} for {2:.8f} {3}.'.format(amount, currency, dogeprice, trade)
###api.buylimit(market, amount, dogeprice)

# Multiplying the price by the multiplier
###dogeprice = round(dogeprice*multiplier, 8)

# Selling 100 DOGE for the  new price
###print 'Selling {0} {1} for {2:.8f} {3}.'.format(amount, currency, dogeprice, trade)
###api.selllimit(market, amount, dogeprice)

# Gets the DOGE balance
###dogebalance = api.getbalance(currency)
###print "Your balance is {0} {1}.".format(dogebalance['Available'], currency)

# For a full list of functions, check out bittrex.py or https://bittrex.com/Home/Api


