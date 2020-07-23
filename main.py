import random
import numpy as np
def main():
    n = int(input("Enter the number of variants "))
    word = input("Enter word ")
    run_genetic(n, word)

def run_genetic(n, word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', ' ']
    words = []
    length = len(word)
    #Initalize words
    for _ in range(0, n):
        new_word = ''
        for _ in range(0, length):
            new_word += random.choice(letters)
        words.append(new_word)
    run = True
    while run:
        fitness_array = evaluate_fitness(words, word)
        print("Words are {} with fitness {}".format(words, fitness_array))
        all_zeroes =  not np.any(fitness_array)
        new_words = []
        midpoint = int(length / 2)
        for _ in range(n):
            # get two parents n times given the fitness probablities
            if(all_zeroes):
                parents = random.choices(words, k=2)
            else:
                parents = random.choices(words, k=2, weights=fitness_array)
            #Crossover and use mutation of 1 percent
            new_word = parents[0][0: midpoint] + parents[1][midpoint: length]
            if new_word == word:
                print("New word found by crossover parents were " + parents[0] + " " + parents[1])
                return True
            mutate_new_word = ''
            for char in new_word:
                val = random.randint(0, 99)
                if val == 1:
                    new_char = random.choice(letters)
                    mutate_new_word += new_char
                    if word == mutate_new_word:
                        print("New word found by mutation parents were " + parents[0] + " " + parents[1])
                        print("And original word was " + new_word)
                        return True
                else:
                    mutate_new_word += char
            new_word = mutate_new_word
            new_words.append(new_word)
        words = new_words





def evaluate_fitness(words, word):
    #create a fitness array use total counts to normalize
    fitness_array = []
    total_counts = 0
    for child in words:
        fitness_score = 0
        for i in range(len(child)):
            if child[i] == word[i]:
                fitness_score+= 1
                total_counts+= 1
        fitness_array.append(fitness_score)
    fitness_array[:] = [x / total_counts if total_counts != 0 else 0 for x in fitness_array]
    return fitness_array




if __name__ == "__main__":
    main()