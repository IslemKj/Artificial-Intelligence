import random
import matplotlib.pyplot as plt

N = 20
LOOPS = 50000


class solution:
    def __init__(self):
        self.gene = [0] * N
        self.utility = 0

'''def test_function( ind ):
        utility1=0
        utility2=0
        for i in range(N):
            utility1 = utility1 + (ind.gene[i]**2)
            utility2 = utility2 + ( 0.5 * (i+1) * ind.gene[i] )
        return (utility1 + (utility2**2) + (utility2**4))   '''
def test_function (ind):
    utility=0
    for i in range (1,N):
        utility = utility + (i*(((2*(ind.gene[i]**2))-ind.gene[i-1])**2))
    return (utility + ((ind.gene[0]-1)**2))


average_best_fitness= []

for _ in range(10):
    utility_values = []
    iterations = []
    

    individual = solution()
    for j in range(N):
        individual.gene[j] = random.randint(-5, 10)
    individual.utility = float('inf')  # Initialize utility with infinity for minimization

    for x in range(LOOPS):
        newind = solution()
        for i in range(N):
            newind.gene[i] = individual.gene[i]

        change_point = random.randint(0, N - 1)
        newind.gene[change_point] = random.randint(0, 100)

        newind.utility = test_function(newind)

        # Change the condition for minimization
        if individual.utility >= newind.utility:
            individual.gene[change_point] = newind.gene[change_point]
            individual.utility = newind.utility

        utility_values.append(individual.utility)
        iterations.append(x)

#print(f'Iteration {x + 1}: Fitness = {individual.utility/LOOPS}')   
    best_fitness = min(utility_values)  # Find the minimum fitness value in utility_values
    print("Best Fitness:", best_fitness)
    average_best_fitness.append(best_fitness)
    
average_fitness = sum(average_best_fitness) / len(average_best_fitness)
print("Average Best Fitness over 10 runs:", average_fitness)
    
    

plt.plot(iterations, utility_values)
plt.xlabel('Iterations')
plt.ylabel('Utility')
plt.grid(True)
plt.show()
