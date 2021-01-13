import matplotlib.pyplot as plt
from annealing_3 import Solver1


def plot_costtemp (temperature, cost_function):
    plt.title('Wartość funkcji kosztu w zależności od temperatury')
    plt.xlabel('Temperatura')
    plt.ylabel('Wartość funkcji kosztu')
    plt.xlim(temperature[0], temperature[-1])
    plt.plot(temperature, cost_function)
    plt.show()



solver = Solver1()
solver.simulated_annealing()

print(solver.temp_results)

plot_costtemp(solver.temp_results, solver.cost_function_results)