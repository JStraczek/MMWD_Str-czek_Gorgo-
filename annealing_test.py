from annealing import Solver


# Plotted tests
solver = Solver()
solver.plot_costepoch()


# Loop test
best_solution=solver.simulated_annealing()
for i in range(10):
    curr_solution=solver.simulated_annealing()
    print("iteration number ",i, "route ",curr_solution[0],'tip= ',curr_solution[1])
    if best_solution[1]<curr_solution[1]:
        best_solution=curr_solution
print("Best solution, route: ",best_solution[0],'tip= ',best_solution[1])