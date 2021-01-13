# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:38:00 2021

@author: Jasiek
"""


import random
import sys
import numpy as np
#from enum import Enum
import math

inf = sys.maxsize

class Order():
    A=(0,'A')
    a=(1,'a')
    B=(2,'B')
    b=(3,'b')
    C=(4,'C')
    c=(5,'c')
    D=(6,'D')
    d=(7,'d')
    E=(8,'E')
    e=(9,'e')
    F=(10,'F')
    f=(11,'f')
    G=(12,'G')
    g=(13,'g')
    H=(14,'H')
    h=(15,'h')
    I=(16,'I')
    i=(17,'i')
    J=(18,'J')
    j=(19,'j')
      
class Solver:
    
    T0 = 10000 # initial temperature
    Tmin = 1 # minimal temperature
    k = 100 # number of iteration per era
    alpha = 0.8 # cooling coefficient
    
    max_prohibited_solutions=300
    
    backpack_volume=3 # backpack volume
    
    restaurants = [Order.A, 	Order.B, 	Order.C, 	Order.D, Order.E] #points of collect
    customers = [Order.a, 	Order.b, 	Order.c, 	Order.d, Order.E] #points of deliver
    
    Xa = [Order.A, Order.a, Order.B, Order.b] # initial solution(route)

    cost_matrix = np.array(
[[	inf	,	3	,	8	,	3	,	9	,	4	,	1	,	10	,	10	,	2	,	4	,	4	,	6	,	8	,	2	,	2	,	6	,	6	,	7	,	3	],
[	inf	,	inf	,	10	,	9	,	9	,	1	,	1	,	8	,	1	,	4	,	3	,	4	,	1	,	5	,	2	,	3	,	5	,	8	,	9	,	1	],
[	10	,	10	,	inf	,	3	,	4	,	7	,	7	,	7	,	6	,	2	,	10	,	1	,	6	,	7	,	4	,	6	,	1	,	5	,	2	,	3	],
[	6	,	6	,	inf	,	inf	,	7	,	5	,	7	,	1	,	5	,	9	,	4	,	8	,	7	,	9	,	8	,	10	,	9	,	1	,	6	,	5	],
[	2	,	5	,	9	,	2	,	inf	,	10	,	10	,	6	,	3	,	9	,	7	,	2	,	8	,	3	,	5	,	8	,	6	,	5	,	4	,	9	],
[	7	,	6	,	8	,	1	,	inf	,	inf	,	10	,	7	,	3	,	8	,	6	,	8	,	8	,	3	,	8	,	6	,	9	,	4	,	8	,	2	],
[	3	,	4	,	1	,	4	,	7	,	7	,	inf	,	5	,	1	,	1	,	7	,	10	,	1	,	4	,	9	,	7	,	3	,	2	,	1	,	1	],
[	10	,	3	,	8	,	2	,	6	,	1	,	inf	,	inf	,	7	,	1	,	1	,	5	,	4	,	2	,	9	,	4	,	4	,	5	,	10	,	2	],
[	9	,	4	,	1	,	5	,	3	,	2	,	7	,	10	,	inf	,	8	,	9	,	4	,	1	,	7	,	4	,	10	,	6	,	8	,	6	,	7	],
[	4	,	1	,	8	,	8	,	1	,	4	,	6	,	10	,	inf	,	inf	,	10	,	10	,	7	,	10	,	6	,	4	,	1	,	7	,	8	,	10	],
[	2	,	3	,	6	,	1	,	9	,	4	,	7	,	6	,	5	,	9	,	inf	,	6	,	8	,	1	,	5	,	9	,	2	,	3	,	3	,	7	],
[	3	,	9	,	7	,	2	,	9	,	2	,	8	,	2	,	7	,	5	,	inf	,	inf	,	5	,	7	,	9	,	9	,	9	,	6	,	6	,	5	],
[	10	,	8	,	1	,	10	,	5	,	7	,	2	,	3	,	7	,	1	,	3	,	6	,	inf	,	10	,	3	,	9	,	7	,	6	,	2	,	8	],
[	9	,	4	,	4	,	3	,	3	,	8	,	10	,	4	,	3	,	7	,	8	,	3	,	inf	,	inf	,	9	,	7	,	9	,	8	,	2	,	4	],
[	8	,	7	,	8	,	6	,	3	,	9	,	8	,	6	,	4	,	1	,	5	,	10	,	1	,	10	,	inf	,	5	,	1	,	2	,	8	,	4	],
[	10	,	7	,	4	,	5	,	1	,	5	,	3	,	6	,	5	,	4	,	10	,	4	,	2	,	4	,	inf	,	inf	,	9	,	3	,	3	,	1	],
[	4	,	7	,	5	,	6	,	9	,	10	,	10	,	9	,	8	,	3	,	6	,	9	,	1	,	8	,	7	,	6	,	inf	,	10	,	4	,	8	],
[	6	,	2	,	7	,	1	,	8	,	10	,	2	,	6	,	8	,	6	,	9	,	5	,	7	,	10	,	4	,	8	,	inf	,	inf	,	7	,	8	],
[	5	,	7	,	7	,	7	,	8	,	6	,	6	,	8	,	2	,	2	,	8	,	3	,	10	,	5	,	8	,	8	,	8	,	3	,	inf	,	6	],
[	6	,	8	,	8	,	10	,	5	,	7	,	4	,	7	,	3	,	9	,	9	,	7	,	7	,	1	,	9	,	7	,	4	,	8	,	inf	,	inf	]]
        ) #bardziej wlasciwa nazwa to time matrix
    
    penalties_matrix= np.array(
                   [[0, 10, 10],
                    [10, 20, 5],
                    [20, 30, 0],
                    [30, 40, -10],
                    [40, 50, -25],
                    [50, inf, -inf]], dtype=object) #bardziej wlasciwa nazwa to cost matrix
    
    def create_init_solution(self):
        c_order=self.restaurants[:]
        d_order=self.customers[:]
        start_point=random.randint(0, len(c_order)-1)
        x_init=[c_order[start_point]]
        backpack=[d_order[start_point]]
        c_order.remove(c_order[start_point])
        d_order.remove(d_order[start_point])
        while len(x_init) != len(self.restaurants + self.customers): # dopóki są zamówienia do odebrania lub do dostarczenia wykonuj
            if len(backpack) < self.backpack_volume: #jeśli ilosc w plecaku < pojemnosci plecaka wykonaj:
                if random.randint(0,1)==0: #tutaj dodamy do sciezki restauracje , // szansa 50% że: wykonaj:
                    if c_order:
                        next_point=0
                        if len(c_order)>1:
                            next_point=random.randint(0, len(c_order)-1)
                        x_init.append(c_order[next_point])
                        backpack.append(d_order[next_point])
                        c_order.remove(c_order[next_point])
                        d_order.remove(d_order[next_point])
                elif backpack: #tutaj dodamy do sciezki klienta
                    next_point=0
                    if len(backpack)>1:
                        next_point=random.randint(0, len(backpack)-1)
                    x_init.append(backpack[next_point])
                    backpack.remove(backpack[next_point])
            else:#musimy dodac do sciezki klienta bo plecak jest pelny
                next_point=random.randint(0, len(backpack)-1)
                x_init.append(backpack[next_point])
                backpack.remove(backpack[next_point])
        return x_init
    
    def check_solution(self, trace):
        total_time=self.calculate_total_time(trace)
        if total_time>50:
            return False #prohibited_soultion
        return True
    
    def calculate_total_time(self, trace):
        time=0
        prev_point=trace[0]
        for point in trace[1:]:
            time+=self.cost_matrix[prev_point[0],point[0]]
            prev_point=point
        return time
    
    def cost_function(self, route):
        cost = 0
        time = 0
        prev_point=route[0]
        for point in route[1:]:
            time+=self.cost_matrix[prev_point[0],point[0]]
            if point[0]%2 !=0:
                for case in self.penalties_matrix:
                    if case[0] < time <= case[1]:
                        cost+= case[2] * (1)
            prev_point=point
        return cost
    
    def get_neighbor_solution(self, route):
        while(self.check_solution(route)):
            place1=random.randint(0,len(route))
            place2=random.randint(0,len(route))
            temp=route[place1]
            route[place1]=route[place2]
            route[place1]=temp
        return route
        
    
    def simulated_annealing(self):
        T = self.T0
        
        #x_init=self.Xa #TODO switch lines
        x_init=self.create_init_solution()#self.restaurants,self.customers)
        limiter=0
        while not self.check_solution(x_init): #uncomment after finisishing create ini solution
            x_init=self.create_init_solution()
            if limiter==self.max_prohibited_solutions:
                print("program nie moze osiagnac dopuszczalnego rozwiazana")
            else:
                limiter+=1
        
        x_star = x_init
        while T > self.Tmin:
            for it in range(self.k):
                x_n=x_star
                while not self.check_solution(x_n):
                    x_n=self.get_neighbor_solution(x_n)
                    limiter=0
                    if limiter==self.max_prohibited_solutions:
                        print("program nie moze osiagnac dopuszczalnego rozwiazana")
                        return None
                    else:
                        limiter+=1
                        
                delta = self.cost_function(x_n) - self.cost_function(x_star)
                
                if delta > 0:
                    x_star=x_n
                else:       
                    r = random.random()
                    if r < math.exp(-delta/T):
                        x_star = x_n
            T *= self.alpha
        return (x_star, self.cost_function(x_star))
        
            
#Xa = [Order.A, Order.a, Order.B, Order.b] # initial solution(route)
        
solver = Solver()
best_solution=solver.simulated_annealing()
for i in range(10):
    curr_solution=solver.simulated_annealing()
    print("iteration number ",i, "route ",curr_solution[0],'tip= ',curr_solution[1])
    if best_solution[1]<curr_solution[1]:
        best_solution=curr_solution
print("Best solution, route: ",best_solution[0],'tip= ',best_solution[1])
    