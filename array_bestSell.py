# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:11:27 2019

@author: yoyau.eo06g
"""

prices=[7,1,5,3,6,4]
#prices=[1,2,3,4,5]
#prices=[7,6,4,3,1]
#prices=[1,2,4,1,3,5]

buy=0
sell=1
tprofit=[]
profit=0
p=0



for i in range(1, len(prices)):
    if prices[i]-prices[buy] > prices[sell]-prices[buy]:
        sell=i
        p=prices[sell]-prices[buy]
        
        buy=i+1
    elif i!=buy:
        buy+=1    