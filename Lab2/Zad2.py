import pygad
import numpy
import time

S = [
    {
        "item": 'zegar',
        "value": 100,
        "weight": 7,
    },
    {
        "item": 'obraz-pejzaż',
        "value": 300,
        "weight": 7,
    },
    {
        "item": 'obraz-portret',
        "value": 200,
        "weight": 6,
    },
    {
        "item": 'radio',
        "value": 40,
        "weight": 2,
    },
    {
        "item": 'laptop',
        "value": 500,
        "weight": 5,
    },
    {
        "item": 'lampka nocna',
        "value": 70,
        "weight": 6,
    },
    {
        "item": 'srebrne sztućce',
        "value": 100,
        "weight": 1,
    },
    {
        "item": 'porcelana',
        "value": 250,
        "weight": 3,
    },
    {
        "item": 'figura z brązu',
        "value": 300,
        "weight": 10,
    },
    {
        "item": 'skórzana torebka',
        "value": 280,
        "weight": 3,
    },
    {
        "item": 'odkurzacz',
        "value": 300,
        "weight": 15,
    },
]

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

# #definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    sum = 0
    totalWeight = 0
    for i in range(len(S)):
        if solution[i] == 1:
            sum += S[i]["value"]
            totalWeight += S[i]["weight"]
    if totalWeight > 25:
        return 0
    else:
        return sum

fitness_function = fitness_func

#ile chromsomów w populacji
#ile genow ma chromosom
sol_per_pop = 11
num_genes = len(S)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 30
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 10

timesum = 0
for i in range(10):
    start = time.time()
    #inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
    ga_instance = pygad.GA(gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes,
                           stop_criteria=["reach_1600"])

    #uruchomienie algorytmu
    ga_instance.run()
    end = time.time()
    timesum += (end - start)

print(timesum / 10)
#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
prediction = ""
for i in range(len(S)):
    if solution[i] == 1:
        prediction += S[i]["item"] + ": " + str(S[i]["value"]) + ", "
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))
print("Number of generations passed is {generations_completed}".format(generations_completed=ga_instance.generations_completed))

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()