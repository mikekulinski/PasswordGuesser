# PasswordGuesser
Uses a genetic algorithm to guess the value of a string

Each generation consists of a specified number of children with the following life cycle:
* Generate new children by randomly sampling letters between random pairs of the best performing guesses
* Mutate a letter of a guess with a specified probability
* Repeat until password has been guessed correctly

Currently, the fitness function is just the percent of correctly guessed letters. Therefore, the guess must have the number of letters of the length of the password. In the future I am going to try to remove this and change the fitness function to edit distance to make it more interesting. I will try to incorporate adding, removing, and swapping operations in order to make this work.
