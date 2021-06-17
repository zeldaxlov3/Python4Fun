#### What's the Number ? ####

import random
number = random.randrange(1, 100)
your_answer = int(input("Your Answer: "))

if your_answer == number:
    print("You've guessed it right")
else:
    print(f"Right answer is {number}, your answer {your_answer}")
if your_answer > 100:
    print("The number is not in range, please type a number less than 100")





