# -*- coding: utf-8 -*-

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
    
class Solver:
    
    T0 = 100 # initial temperature
    Tmin = 1 # minimal temperature
    k = 10 # number of iteration per era
    alpha = 0.8 # cooling coefficient
    
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

    def simulated_annealing(self):
        T = self.T0 
        x_star = self.Xa[:]
        cost_star = self.cost_function(x_star)
        while T > self.Tmin:
            for i in range(self.k):
                xn = self.get_neighbor_solution(x_star)
                delta = self.cost_function(xn) - cost_star
                if delta <= 0:
                    x_star = xn
                    cost_star = self.cost_function(x_star)
                else:
                    r = random.random()
                    if r < math.exp(-delta/T):
                        x_star = xn
                        cost_star = self.cost_function(x_star)   
            T *= self.alpha
    
    def get_neighbor_solution(self, x_star):
        
        for i in range (1,len(x_star)):
            x_star_new=copy.copy(x_star)

            if self.calculate_traverse_cost(x_star_new[i],x_star_new[i+1])>self.calculate_traverse_cost(x_star_new[i-1],x_star_new[i]):
                temp=x_star_new[i-1]
                x_star_new[i-1]=x_star_new[i]
                x_star_new[i]=temp
                time=self.total_time(x_star_new)
                if self.check_solution(time):
                    if random.random()>0.8:
                        return x_star_new
                return x_star
    
    def check_solution(self, cost):
        if cost>50:
            return False #prohibited_soultion
        return True
        
    def total_time(self, x_star):
        cost = 0
        for order in self.orders:
            time_cost = self.calculate_order_cost(order, x_star)
            cost += time_cost
        return cost
    
    
    
    def cost_function(self, x_star):
        cost = 0
        for order in self.orders:
            time_cost = self.calculate_order_cost(order, x_star)
            single_cost = self.calculate_penalty(time_cost)
            cost += single_cost
        
        return cost

    def calculate_order_cost(self, order, Xa): # returns order realisation cost based on solution Xa
        cost = 0
        for i in range(1, len(Xa)):
            cost += self.calculate_traverse_cost(Xa[i-1], Xa[i])
            print('cost',cost)
            if Xa[i][1] == order[1].lower():
                break
        
        return cost
    
    def calculate_traverse_cost(self, p1, p2): # returns cost of traversing between 2 points from cost_matrix
        return self.cost_matrix[ p1[0] ][ p2[0] ]

    def calculate_penalty(self, time):
        for case in self.penalties_matrix:
            if case[0] < time <= case[1]:
                
                return case[2] * (1)
            
    def get_order_list(self):
        order_list = []
        for el in self.Xa:
            if el[1].isupper():
                order_list.append(el)
        
        return order_list


     
solver = Solver()
solver.simulated_annealing()