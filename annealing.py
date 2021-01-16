import matplotlib.pyplot as plt
import random
import sys
import numpy as np
import math

inf = sys.maxsize*2 + 1

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

    cost_matrix = np.array(

    [[	inf	,	3	,	10	,	6	,	2	,	7	,	3	,	10	,	9	,	4	,	2	,	3	,	10	,	9	,	8	,	10	,	4	,	6	,	5	,	6	],
    [	inf	,	inf	,	10	,	6	,	5	,	6	,	1	,	8	,	1	,	4	,	3	,	4	,	1	,	5	,	2	,	3	,	5	,	8	,	9	,	1	],
    [	10	,	10	,	inf	,	3	,	4	,	7	,	7	,	7	,	6	,	2	,	10	,	1	,	6	,	7	,	4	,	6	,	1	,	5	,	2	,	3	],
    [	6	,	6	,	inf	,	inf	,	7	,	5	,	7	,	1	,	5	,	9	,	4	,	8	,	7	,	9	,	8	,	10	,	9	,	1	,	6	,	5	],
    [	2	,	5	,	4	,	7	,	inf	,	10	,	10	,	6	,	3	,	9	,	7	,	2	,	8	,	3	,	5	,	8	,	6	,	5	,	4	,	9	],
    [	7	,	6	,	7	,	5	,	inf	,	inf	,	10	,	7	,	3	,	8	,	6	,	8	,	8	,	3	,	8	,	6	,	9	,	4	,	8	,	2	],
    [	3	,	1	,	7	,	7	,	10	,	10	,	inf	,	5	,	1	,	1	,	7	,	10	,	1	,	4	,	9	,	7	,	3	,	2	,	1	,	1	],
    [	10	,	8	,	7	,	1	,	6	,	7	,	inf	,	inf	,	7	,	1	,	1	,	5	,	4	,	2	,	9	,	4	,	4	,	5	,	10	,	2	],
    [	9	,	1	,	6	,	5	,	3	,	3	,	1	,	7	,	inf	,	8	,	9	,	4	,	1	,	7	,	4	,	10	,	6	,	8	,	6	,	7	],
    [	4	,	4	,	2	,	9	,	9	,	8	,	1	,	1	,	inf	,	inf	,	10	,	10	,	7	,	10	,	6	,	4	,	1	,	7	,	8	,	10	],
    [	2	,	3	,	10	,	4	,	7	,	6	,	7	,	1	,	9	,	10	,	inf	,	6	,	8	,	1	,	5	,	9	,	2	,	3	,	3	,	7	],
    [	3	,	4	,	1	,	8	,	2	,	8	,	10	,	5	,	4	,	10	,	inf	,	inf	,	5	,	7	,	9	,	9	,	9	,	6	,	6	,	5	],
    [	10	,	1	,	6	,	7	,	8	,	8	,	1	,	4	,	1	,	7	,	8	,	5	,	inf	,	10	,	3	,	9	,	7	,	6	,	2	,	8	],
    [	9	,	5	,	7	,	9	,	3	,	3	,	4	,	2	,	7	,	10	,	1	,	7	,	inf	,	inf	,	9	,	7	,	9	,	8	,	2	,	4	],
    [	8	,	2	,	4	,	8	,	5	,	8	,	9	,	9	,	4	,	6	,	5	,	9	,	3	,	9	,	inf	,	5	,	1	,	2	,	8	,	4	],
    [	10	,	3	,	6	,	10	,	8	,	6	,	7	,	4	,	10	,	4	,	9	,	9	,	9	,	7	,	inf	,	inf	,	9	,	3	,	3	,	1	],
    [	4	,	5	,	1	,	9	,	6	,	9	,	3	,	4	,	6	,	1	,	2	,	9	,	7	,	9	,	1	,	9	,	inf	,	10	,	4	,	8	],
    [	6	,	8	,	5	,	1	,	5	,	4	,	2	,	5	,	8	,	7	,	3	,	6	,	6	,	8	,	2	,	3	,	inf	,	inf	,	7	,	8	],
    [	5	,	9	,	2	,	6	,	4	,	8	,	1	,	10	,	6	,	8	,	3	,	6	,	2	,	2	,	8	,	3	,	4	,	7	,	inf	,	6	],
    [	6	,	1	,	3	,	5	,	9	,	2	,	1	,	2	,	7	,	10	,	7	,	5	,	8	,	4	,	4	,	1	,	8	,	8	,	inf	,	inf	]]
            ) 

    T0 = 10000 # initial temperature
    Tmin = 1 # minimal temperature
    k = 10 # number of iteration per era
    alpha = 0.8 # cooling coefficient

    order_amount = 5
    max_prohibited_solutions=500
    max_time = order_amount * 10
    scaler = max_time / 50

    penalties_matrix= np.array(
                [[0*scaler, 10*scaler, 20],
                [10*scaler, 20*scaler, 10],
                [20*scaler, 30*scaler, 5],
                [30*scaler, 40*scaler, 0],
                [40*scaler, 50*scaler, -10],
                [50*scaler, inf, -inf]], dtype=object) 
    
    backpack_volume=3 # backpack volume
    restaurants = [Order.A, Order.B, Order.C, Order.D, Order.E, Order.F, Order.G, Order.H, Order.I, Order.J] #points of collect
    customers = [Order.a, Order.b, Order.c, Order.d, Order.e, Order.f, Order.g, Order.h, Order.i, Order.j] #points of deliver

    restaurants = restaurants[0:order_amount]
    customers = customers[0:order_amount]

    cost_function_out = []

    
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

                x_n=self.get_neighbor_solution(x_star)
                while not self.check_solution(x_n):
                    x_n=self.get_neighbor_solution(x_n)
                    limiter=0
                    if limiter==self.max_prohibited_solutions:
                        print("program nie moze osiagnac dopuszczalnego rozwiazana")
                    else:
                        limiter+=1

                delta = self.cost_function(x_n) - self.cost_function(x_star)

                if delta > 0:
                    x_star=x_n
                else:       
                    r = random.random()
                    e = math.exp(delta/T)
                    if r < e:
                        x_star = x_n
                self.cost_function_out.append(self.cost_function(x_star))
            T *= self.alpha
        return (x_star, self.cost_function(x_star))
    
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
                        next_point = 0
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
    
    def check_solution(self, route): 
        if route[0][1].islower():
            return False
        else: 
            tmp = [route[0]]

        for el in route[1:]:
            if el[1].islower() and (el[0] - 1, el[1].upper()) not in tmp:
                return False
            elif el[1].isupper():
                tmp.append(el)
        
        backpack = 0
        for el in route:
            if el[1].isupper():
                backpack+=1
            else:
                backpack-=1
            if backpack > self.backpack_volume:
                return False


        time=0
        prev_point=route[0]
        for point in route[1:]:
            time+=self.cost_matrix[prev_point[0],point[0]]
            prev_point=point

        if time>self.max_time:
            return False #prohibited_solution

        return True
    

    def cost_function(self, x_star):
        cost = 0
        for order in self.restaurants:
            time_cost = self.calculate_order_cost(order, x_star)
            cost += self.calculate_penalty(time_cost)
        
        return cost

    def calculate_order_cost(self, order, Xa): # returns order realisation cost based on solution Xa
        cost = 0
        for i in range(1, len(Xa)):
            cost += self.cost_matrix[Xa[i-1][0], Xa[i][0]]
            
            if Xa[i][1] == order[1].lower():
                break
    
        return cost

    def calculate_penalty(self, time):
        for case in self.penalties_matrix:
            if case[0] < time <= case[1]:
                return case[2]


    def get_neighbor_solution(self, route):
        new_route = route[:]
        place1=random.randint(0,len(new_route)-1)
        place2=random.randint(0,len(new_route)-1)
        new_route[place1], new_route[place2] = new_route[place2], new_route[place1]
        return new_route


    def plot_costepoch (self):
        self.simulated_annealing()
        plt.title('Wartość funkcji kosztu w zależności od epoki')
        plt.xlabel('Nr epoki') 
        plt.ylabel('Wartość funkcji kosztu')
        plt.plot([x for x in range(len(self.cost_function_out))], self.cost_function_out)
        plt.show()
    


        