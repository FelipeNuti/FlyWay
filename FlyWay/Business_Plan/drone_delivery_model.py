# -*- coding: utf-8 -*-
"""
New drone
"""

def expgrow(var, time, i):
    return var* (1+i)**(time/360)

pi = 3.1415926535897932384626433832795028841971

constant = 1.24

class city:
    def __init__(self, pop, period, area, price_kwh, work_day, k, infrastructure_cost, minwage):
        self.pop = pop
        self.period = period
        self.area = area
        self.price_kwh = price_kwh
        self.work_day = work_day
        self.k = k
        self.radius = (self.area/pi)**0.5
        self.mean_distance =  (constant) * self.radius
        self.infrastructure_cost_per_day = infrastructure_cost/30
        self.minwage = minwage
       
        
class drone:
    def __init__(self, autonomy, speed, bat_charge, bat_tension, bat_time, price_drone):
        self.autonomy = autonomy
        self.speed = speed
        self.bat_charge = bat_charge
        self.bat_tension = bat_tension
        self.bat_time = bat_time
        self.price_drone = price_drone
        self.bat_energy = self.bat_charge * self.bat_tension/1000000
        self.max_distance = 0.5 * self.speed * (self.autonomy/60)
        
    
class context:
    def __init__(self, city, drone, time, rate, drones_had):
        self.efpop = min(city.pop, city.pop * (2*drone.max_distance/(constant*city.radius))**2)
        self.ef_mean_distance = min(drone.max_distance*2, city.mean_distance)
        self.dialy_demand =  expgrow(((self.efpop*city.k)/city.period), time, rate)
        self.city = city
        self.drone = drone
        self.rate = rate
        self.drones_had = drones_had
        self.avg_delivery_time = 2*self.ef_mean_distance/drone.speed #average delivery time in hours
        self.del_p_opcy = 2* drone.max_distance/self.ef_mean_distance #deliveries per operation cycle
        self.op_cycle = self.del_p_opcy*(self.avg_delivery_time)+drone.bat_time #hours per operation cycle (between two charges)
        self.bat_price = drone.bat_energy* city.price_kwh #price to charge 1 drone once
        self.del_per_day = (city.work_day/self.op_cycle) * self.del_p_opcy #deliveries a drone makes, on average, in one day
        self.energy_per_day = self.del_per_day * drone.bat_energy #kwh spent per day per drone
        self.price_per_day = self.energy_per_day * city.price_kwh #money spent on charging the drone in one day
        self.drones_needed = int(self.dialy_demand/self.del_per_day)
        self.energy_expense = self.price_per_day * self.drones_needed #total money spent on energy spent in 1 day
        self.drone_expense = drone.price_drone * (self.drones_needed - drones_had)
        self.staff_num = int(self.dialy_demand/(5*city.work_day)) + 1
        self.staff_expense_per_day = (self.city.minwage * self.staff_num)/30
        

class company:
    def __init__(self, cont, time_company, time_to_break_even, actual_price_charged):
        self.time_to_break_even = time_to_break_even
        self.actual_price_charged = actual_price_charged
        self.cont = cont
        self.time_company = time_company
        income = 0
        expense = 0
        drones_had = 0
        for time in range(0, self.time_company):
            cnt = context(cont.city, cont.drone, time, cont.rate, drones_had)
            income += self.actual_price_charged*(cnt.dialy_demand)
            expense += (cnt.staff_expense_per_day + cnt.city.infrastructure_cost_per_day + cnt.drone_expense + cnt.energy_expense)
            drones_had = cnt.drones_needed
            
        self.income = income
        self.expense = expense
        self.profit = income - expense





