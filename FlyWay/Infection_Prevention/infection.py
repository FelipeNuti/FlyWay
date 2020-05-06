"""
Studying the infection risk
"""

# =============================================================================
# --Any person might be infected or not, with a given probability determined by the
# stage of the pandemic. 
# --If somebody is infected, they have a fixed probability of transmitting the virus
# via air to someone else, and another probability by contact.
# --The probability for someone to transmit the virus via contact is the same as 
# the probability of the person infecting a surface.
# --Each person receiving the infection has a probability of getting rid of the virus
# by washing their hands (and simmilar preventive measures)
# --From the ICL article: R0 is estimated to be between 2 and 6. 
# --The percentage of infectives at a given moment ranges between 0 and 1 - 1/R0 
# make estimate based on that.
# --Each deliverer might get infected in one of his deliveries
# =============================================================================

import numpy.random as random
import matplotlib.pyplot as plt
import numpy as np

def union(p1, p2):
    return p1 + p2 - p1*p2

percent_infected = 0.2 #percent of the population already infected

prob_air = 0.3 #probability of airborne infection
prob_contact = 0.6 #probability of contact infection

mult_contact_mitigation = 0.2 #how much of the initial risk is left after preventive measures are taken

num_deliveries = 1000
num_deliverers = 10

infected_deliv = random.choice([True, False], num_deliverers, p = [percent_infected, 1-percent_infected])

new_inf_count = 0

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
        new_inf_count += 1
        
        
    
    





