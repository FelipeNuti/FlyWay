# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:37:22 2020

@author: 10
"""

import new_drone as d
import matplotlib.pyplot as plt

city = d.city
drone = d.drone
context = d.context
company = d.company

pop = 3303786 #1752000 #3303786
area = 7626 #525
price = 1435
autonomy = 28
battery = 6000
speed = 60
tension = 15.2
salary = 1000
rate = 0.075
charged = 4
numtest = 1000
tcomp = 360
start_cost = 0
plt.xlabel("Fraction of adopters in the population")
plt.ylabel("Money (EUR)")

# Data for Budapest:
BP = city(pop ,
          5,
          area,
          0.1161,
          8,
          0.001, 
          3600, 
          salary)


dr = drone(autonomy,
           speed,
           battery,
           tension,
           1,
           price)

cnt = context(BP, dr, 0, rate, 0)

BPcomp = company(cnt, tcomp, 60, charged)

def plot_k():
    ar_k = []
     
    ar_prof = []
    ar_exp = []
    ar_inc = []
      
    for k in range(1, int(int(numtest/10))):
        BP = city(pop ,
              5,
              area,
              0.1161,
              8,
              k/numtest, 
              3600, 
              salary)
        cnt = context(BP, drone(autonomy,speed,battery,tension,1,price), 0, rate, 0)
        BPcomp = company(cnt, tcomp, 60, charged)
        ar_k.append(k/numtest)
        ar_prof.append(BPcomp.income - BPcomp.expense - start_cost)
        ar_inc.append(BPcomp.income)
        ar_exp.append(BPcomp.expense + start_cost)
        
    plt.xlabel("Fraction of adopters in the population")
    plt.ylabel("Money (EUR)")
    #plt profit
    plt.plot(ar_k, ar_prof, color = 'black')
    plt.plot(ar_k, ar_exp, color = 'red')
    plt.plot(ar_k, ar_inc, color = 'green')
    
    m_prof = (ar_prof[-1] - ar_prof[0])/(ar_k[-1] - ar_k[0])
    m_exp = (ar_exp[-1] - ar_exp[0])/(ar_k[-1] - ar_k[0])
    rri = m_prof/m_exp
    print(rri)
    



def plot_t():
    ar_k2 = []
     
    ar_prof2 = []
    ar_exp2 = []
    ar_inc2 = []
    for k in range(1, 10*360):
        BP = city(pop ,
              5,
              area,
              0.1161,
              8,
              0.0122, 
              3600, 
              salary)
        cnt = context(BP, drone(autonomy,speed,battery,tension,1,price), 0, rate, 0)
        BPcomp = company(cnt, k, 60, charged)
        ar_k2.append(k/360)
        ar_prof2.append(BPcomp.income - BPcomp.expense - start_cost)
        ar_inc2.append(BPcomp.income)
        ar_exp2.append(BPcomp.expense + start_cost)
    
    plt.xlabel("Years since the start of the company")
    plt.ylabel("Money (EUR)")
    #plt profit
    plt.plot(ar_k2, ar_prof2, color = 'black')
    plt.plot(ar_k2, ar_exp2, color = 'red')
    plt.plot(ar_k2, ar_inc2, color = 'green')

BP = city(pop ,
          5,
          area,
          0.1161,
          8,
          0.0122, 
          3600, 
          salary)


dr = drone(autonomy,
           speed,
           battery,
           tension,
           1,
           price)

cnt = context(BP, dr, 0, rate, 0)

BPcomp = company(cnt, tcomp, 60, charged)