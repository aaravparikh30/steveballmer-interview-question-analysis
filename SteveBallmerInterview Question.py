import random
from collections import Counter
import matplotlib.pyplot as plt

def highlow(num, target):
    if num > target:
        return "high"
    elif num < target:
        return "low"
    else:
        return "correct"

def execution(randnumber):
    storage = [0, 100]
    count = 1
    guess = (storage[0] + storage[1]) // 2
    feedback = highlow(guess, randnumber)

    while feedback != "correct":
        count += 1
        if feedback == "high":
            storage[1] = guess
        else:
            storage[0] = guess
        guess = (storage[0] + storage[1]) // 2

        if storage[1] - storage[0] <= 1:
            guess = randnumber
            break

        feedback = highlow(guess, randnumber)

    return count

# Run the simulation 1,000,000 times
results = [execution(random.randint(1, 100)) for _ in range(1_000_000)]

# Count frequency of number of tries
distribution = Counter(results)

# Plotting
plt.bar(distribution.keys(), distribution.values())
plt.xlabel('Number of Guesses')
plt.ylabel('Frequency')
plt.title('Guess Distribution Over 1,000,000 Runs')
plt.grid(True)
plt.show()

distribution.most_common()



#__________________________________________________________________----------PRE-GPT-VERSIONS---------___________________

# import numpy as np
# import random

# randnumber = random.randint(1, 100)

# def highlow(num):
#     if num > randnumber:
#         return "high"
#     elif num < randnumber:
#         return "low"
#     else:
#         return "correct"

# def execution():
#     storage = [0, 100]
#     count = 1
#     guess = (storage[0] + storage[1]) // 2
#     feedback = highlow(guess)

#     while feedback != "correct":
#         count += 1

#         if feedback == "high":
#             storage[1] = guess
#         else:
#             storage[0] = guess

#         # Update guess
#         guess = (storage[0] + storage[1]) // 2

#         # 🔐 Safety net: if we're within 1, just assume we hit the number
#         if storage[1] - storage[0] <= 1:
#             guess = randnumber  # Force break condition
#             break

#         feedback = highlow(guess)

#     #print(f"Guessed correctly: {guess} in {count} tries. Randomnly generated number was {randnumber}.")
#     return count
# total = []
# for i in range(1000):
#     newcount = (execution())
#     total.append(newcount)

# print(total)
    

# print('Simulation Complete')



#SHITTY BASIC INEFFICIENT VERSION

# def probabilities():
#     guess = 50
#     if randnumber > 50:
#         guess = 51
#     else:
#         guess = 0
#     count = 1
#     while guess != randnumber:
#         count += 1
#         guess += 1
#     print('done')
#     print('This took you' + str(count) + ' tries')
#     return ('Your guess was ' + str(guess) + ' and the real number was ' + str(randnumber))

# print(probabilities())
    
    