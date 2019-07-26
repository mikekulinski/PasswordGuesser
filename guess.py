import random
import string


class Guess:
    def __init__(self, password, guess=None):
        if guess:
            self.guess = guess
        else:
            self.guess = self.getGuess(len(password))
        self.password = password

    def getGuess(self, length):
        guess = ""
        for j in range(length):
            guess += random.choice(string.ascii_letters)

        return guess

    def fitness(self):
        fitness = 0
        for i in range(len(self.password)):
            if self.guess[i] == self.password[i]:
                fitness += 1

        return fitness

    def mutate(self, chance_of_mutation):
        for i in range(len(self.guess)):
            if random.random() <= chance_of_mutation:
                self.guess = (
                    self.guess[:i]
                    + random.choice(string.ascii_letters)
                    + self.guess[i + 1 :]
                )
