import random
import sys
import numpy as np
from enum import Enum
 

inf = sys.maxsize

class Order(Enum):
    A = (0, 'A')
    a = (1, 'a')
    B = (2, 'B')
    b = (3, 'b')
    C = (4, 'C')
    c = (5, 'c')

class Solver:
    

    T0 = 100 # initial temperature
    Xa = [Order.A, Order.a, Order.B, Order.b] # initial solution

    cost_matrix = np.array([[inf, 10, 5, 15],
                [inf, inf, 5, 5],
                [5, 5, inf, 10],
                [15, 5, inf, inf]])
    
    penalties_matrix= np.array([[0, 10, 10],
                    [10, 20, 5],
                    [20, 30, 0],
                    [30, 40 -10],
                    [40, 50, -25],
                    [50, inf, -inf]])

    def cost_function(self):
        cost = 0
        orders = self.get_order_list()
        for order in orders:
            cost += self.calculate_order_cost(order)
        
        return cost


    def calculate_order_cost(self, order): # returns order realisation cost based on solution Xa
        cost = 0
        for i in range(1, len(self.Xa)):
            cost += self.calculate_traverse_cost(self.Xa[i-1], self.Xa[i])
            
            if self.Xa[i].value[1] == order.value[1].lower():
                break
    
        return cost

    
    def calculate_traverse_cost(self, p1, p2): # returns cost of traversing between 2 points from cost_matrix
        return self.cost_matrix[ p1.value[0] ][ p2.value[0] ]


    def get_order_list(self) -> list:
        order_list = []
        for el in self.Xa:
            if el.value[1].isupper():
                order_list.append(el)
        
        return order_list

   
solver = Solver()
print(solver.cost_function())