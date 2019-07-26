import random
import string
from guess import Guess


def initPopulation(size, password):
    population = []

    for _ in range(size):
        population.append(Guess(password))

    return population


def crossover(population, password, number_of_best, number_of_children):
    assert ((number_of_best) / 2 * number_of_children) == len(
        population
    ), "Population will not stay constant!"
    best = sorted(population, key=lambda x: x.fitness(), reverse=True)[:number_of_best]

    parents = best
    random.shuffle(parents)
    children = []
    for i in range(0, len(parents), 2):
        for _ in range(number_of_children):
            child = ""
            for j in range(len(password)):
                child += parents[i + random.randint(0, 1)].guess[j]

            children.append(Guess(password, child))

    return children


def mutate(population, chance_of_mutation):
    for p in population:
        p.mutate(chance_of_mutation)

    return population


def getBestFitness(population):
    best = sorted(population, key=lambda x: x.fitness(), reverse=True)[0]
    return best.fitness()


def guessPassword(
    password, population_size, number_of_best, number_of_children, chance_of_mutation
):
    population = initPopulation(population_size, password)
    bestFitness = getBestFitness(population)
    generation = 0
    print("Generation: " + str(generation) + ", Best Fitness: " + str(bestFitness))

    while bestFitness < len(password):
        children = crossover(population, password, number_of_best, number_of_children)
        population = mutate(children, chance_of_mutation)
        bestFitness = getBestFitness(population)
        generation += 1

        print("Generation: " + str(generation) + ", Best Fitness: " + str(bestFitness))

    return sorted(population, key=lambda x: x.fitness(), reverse=True)[0].guess


population_size = 200
password = "asdipobasbculobeuwoiubvcasklseiuasdgbwerbwergaspovurpoucnp"
number_of_best = 80
number_of_children = 5
chance_of_mutation = 0.01
print(
    "Final guess: "
    + guessPassword(
        password,
        population_size,
        number_of_best,
        number_of_children,
        chance_of_mutation,
    )
)
