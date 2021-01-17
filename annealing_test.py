from annealing import Solver
import matplotlib.pyplot as plt
from time import time
solver = Solver()

"""
# # Plotted tests
solver.plot_costepoch()


# Loop test
best_solution=solver.simulated_annealing()
print("iteration number ",0, "route ",best_solution[0],'tip= ',best_solution[1])
for i in range(10):
    curr_solution=solver.simulated_annealing()   
    print("iteration number ",i+1, "route ",curr_solution[0],'tip= ',curr_solution[1])
    if best_solution[1]<curr_solution[1]:
        best_solution=curr_solution
print("Best solution, route: ",best_solution[0],'tip= ',best_solution[1])


#cost function test
solutions=[]
average=0
iterations=100
max_val=0
for i in range(iterations):
    curr_solution=solver.simulated_annealing()   
    solutions.append(curr_solution)
    average+=curr_solution[1]
    if curr_solution[1]>max_val:
        max_val=curr_solution[1]

plt.title('Wartość funkcji kosztu w {} iteracjach przy {} epokach'.format(iterations, solver.k))
plt.xlabel('Nr iteracji') 
plt.ylabel('Wartość funkcji kosztu')
plt.plot([x for x in range(1,len(solutions)+1)], [y[1] for y in solutions])
plt.show()
print("Wartosc srednia przy {} epoce: {}".format(solver.k, average/iterations))
print("Wartosc maksymalna przy {} epoce: {}".format(solver.k, max_val))
"""
"""
#time test
average_time=0
iterations=10
time_list=[]
max_time=0
min_time=10000

for i in range(iterations):
    t_start=time()
    curr_solution=solver.simulated_annealing()
    t_end=time()
    time_it=t_end-t_start
    time_list.append(time_it)
    average_time+=(time_it)
    if time_it>max_time:
        max_time=time_it
    if time_it<min_time:
        min_time=time_it
        
plt.title('Czas potrzebny na wykonanie iteracji przy {} klientach'.format(solver.order_amount))
plt.xlabel('Nr iteracji') 
plt.ylabel('Czas wykonywania algorytmu[s]')
plt.plot([x for x in range(1,len(time_list)+1)], [y for y in time_list], 'go')
plt.show()
print("Sredni czas pracy {}s przy {} klientach".format(average_time/iterations, solver.order_amount))
print("Maksymalny czas pracy {}s przy {} klientach".format(max_time,solver.order_amount))
print("Minimalny czas pracy {}s przy {} klientach".format(min_time,solver.order_amount))

y=[0.026965689659118653,0.0554433012008667,0.17973413944244385,0.8948489761352539,7.183250594139099,47.00067026615143]
x=[5,6,7,8,9,10]
plt.title('Czas potrzebny na wykonanie iteracji w zależnosci od ilosci klientow')
plt.xlabel('Liczba klientow') 
plt.ylabel('Czas wykonywania algorytmu[s]')
plt.plot(x, y, 'go')
plt.show()
"""

#cost function test
solutions=[]
average=0
iterations=100
max_val=0
for i in range(iterations):
    curr_solution=solver.simulated_annealing()   
    solutions.append(curr_solution)
    average+=curr_solution[1]
    if curr_solution[1]>max_val:
        max_val=curr_solution[1]

plt.title('Wartość funkcji kosztu w {} iteracjach przy T_pocz={}'.format(iterations, solver.T0))
plt.xlabel('Nr iteracji') 
plt.ylabel('Wartość funkcji kosztu')
plt.plot([x for x in range(1,len(solutions)+1)], [y[1] for y in solutions])
plt.show()
print("Wartosc srednia {} przy temperaturze początkowej={}".format(average/iterations,solver.T0))
print("Wartosc maksymalna {} przy temperaturze początkowej={}".format(max_val,solver.T0))

