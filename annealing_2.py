# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:38:00 2021

@author: Jasiek
"""


import random
import sys
import copy
import numpy as np
from enum import Enum
import math

inf = sys.maxsize

class Order():
    A = (0, 'A')
    a = (1, 'a')
    B = (2, 'B')
    b = (3, 'b')
    C = (4, 'C')
    c = (5, 'c')
    
class Solver1:
    
    T0 = 100 # initial temperature
    Tmin = 10 # minimal temperature
    k = 2 # number of iteration per era
    alpha = 0.8 # cooling coefficient
    
    max_prohibited_solutions=300
    
    backpack_volume=3 # backpack volume
    
    orders = [Order.A, Order.B] #initial solution
    
    Xa = [Order.A, Order.a, Order.B, Order.b] # initial solution(route)

    cost_matrix = np.array(
               [[inf, 10, 5, 15],
                [inf, inf, 5, 5],
                [5, 5, inf, 10],
                [15, 5, inf, inf]]) 
    
    penalties_matrix= np.array(
                   [[0, 10, 10],
                    [10, 20, 5],
                    [20, 30, 0],
                    [30, 40, -10],
                    [40, 50, -25],
                    [50, inf, -inf]], dtype=object)
    
    """def create_init_solution(orders):
        Xa=[]
        Xa.append"""
    
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
            """print("temp",temp)
            print(prev_point)
            print(point)
            print(time)"""
            prev_point=point
        return time
            
            
    """
    def cost_function(self, x_star):
        cost = 0
        for order in self.orders:
            time_cost = self.calculate_order_cost(order, x_star)
            single_cost = self.calculate_penalty(time_cost)
            cost += single_cost
        return cost
    
    def calculate_traverse_cost(self, p1, p2): # returns cost of traversing between 2 points from cost_matrix
        return self.cost_matrix[ p1[0] ][ p2[0] ]
    
    def calculate_order_cost(self, order, Xa): # returns order realisation cost based on solution Xa
        cost = 0
        for i in range(1, len(Xa)):
            cost += self.calculate_traverse_cost(Xa[i-1], Xa[i])
            print('cost',cost)
            if Xa[i][1] == order[1].lower():
                break
        return cost    
    """
    def simulated_annealing(self):
        T = self.T0
        
        x_init=self.Xa #TODO switch lines
        """
        x_init=create_init_solution(self.orders)
        limiter=0
        while not check_solution(x_init): #uncomment after finisishing create ini solution
            x_a=create_init_solution(self.orders)
            if limiter==max_prohibited_solutions:
                print("program nie moze osiagnac dopuszczolnego rozwiazana")
            else:
                limiter+=1
        """
        x_star = x_init
        while T > self.Tmin:
            for it in range(self.k):
                x_n=x_star
                while not self.check_solution(x_n):
                    #x_n=zmiana w rozwiazaniu
                    limiter=0
                    if limiter==max_prohibited_solutions:
                        print("program nie moze osiagnac dopuszczolnego rozwiazana")
                    else:
                        limiter+=1
                        
                delta = self.cost_function(x_n) - self.cost_function(x_star)
                
                if delta > 0:
                    x_star=x_n
                else:       
                    r = random.random()
                    if r < math.exp(-delta/T):
                        x_star = xn
            T *= self.alpha
        
            
#Xa = [Order.A, Order.a, Order.B, Order.b] # initial solution(route)
solver = Solver1()
solver.simulated_annealing()