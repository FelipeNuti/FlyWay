#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
functions to plot contagion data
"""

import numpy.random as random
import matplotlib.pyplot as plt
import numpy as np

def union(p1, p2):
    return p1 + p2 - p1*p2

def test_traditional(percent_infected, 
                     prob_air, 
                     prob_contact, 
                     mult_contact_mitigation,
                     num_deliveries,
                     num_deliverers):
    
    new_inf_count = 0
    for t in range(0, 99):
        infected_deliv = random.choice([True, False], num_deliverers, p = [percent_infected, 1-percent_infected])
        for i in range(1, num_deliveries):
            person_inf = random.choice([True, False], 1, p = [percent_infected, 1-percent_infected])[0]
            d_id = random.choice(range(0, num_deliverers - 1), 1)[0]
            deliv_inf = infected_deliv[d_id]
            if (person_inf and not deliv_inf):
                p_del_get_inf = union(prob_air, prob_contact*mult_contact_mitigation)
                d_gets_inf = random.choice([True, False], 1, p = [p_del_get_inf, 1-p_del_get_inf])
                infected_deliv[d_id] = infected_deliv[d_id] and d_gets_inf
            
            elif ((not person_inf) and (deliv_inf)):
                p_per_get_inf = union(prob_air, prob_contact*mult_contact_mitigation)
                per_gets_inf = random.choice([True, False], 1, p = [p_per_get_inf, 1-p_per_get_inf])
                if per_gets_inf:
                    new_inf_count += 1
            
    return (new_inf_count/num_deliveries)/100

def plot_traditional(R0,
                     prob_air, 
                     prob_contact, 
                     mult_contact_mitigation,
                     num_deliveries,
                     num_deliverers, 
                     plot_color):
    
    pc = 1 - (1/R0)
    ttt_pc = int(pc*100)
    x = []
    y = []
    
    for i in range(0, ttt_pc):
        nic = test_traditional(i/100, 
                             prob_air, 
                             prob_contact, 
                             mult_contact_mitigation,
                             num_deliveries,
                             num_deliverers)
        x.append(i/100)
        y.append(nic)
    
    plt.xlabel("Percent of population infected")
    plt.ylabel("Percent of customers infected with deliveries")
    plt.plot(x, y, plot_color)
    plt.show()
    plt.ylim(0.00, 0.10)
    
    
def plot_drone(R0, 
             prob_contact, 
             mult_contact_mitigation,
             num_deliveries,
             num_deliverers, plot_color):
#    Drone
    
    plot_traditional(R0,
                     0, 
                     prob_contact, 
                     mult_contact_mitigation,
                     num_deliveries,
                     num_deliverers,
                     plot_color)
    
    plt.ylim(0.00, 0.10)
    

def plot_together(R0,
                 prob_air, 
                 prob_contact, 
                 mult_contact_mitigation,
                 num_deliveries,
                 num_deliverers,
                 trad_color,
                 drone_color):
    
    plot_traditional(R0,
                     prob_air, 
                     prob_contact, 
                     mult_contact_mitigation,
                     num_deliveries,
                     num_deliverers,
                     trad_color)
    
    plot_drone(R0, 
             prob_contact, 
             mult_contact_mitigation,
             num_deliveries,
             num_deliverers,
             drone_color)
    
    