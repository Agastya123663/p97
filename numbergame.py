import random
chances = 0
number = random.randint(1,10)
while(chances<=5):
    guess = int(input('Guess the number, hint - it is between 1-10 : '))
    chances = chances + 1
    if(guess<number):
        print('You are close , just guess a bit higher')
    if(guess>number):
        print('You are close , just guess a bit lower')
    if(guess==number):
        print('You won congratulations')
        break
    if(chances==5):
        print('Sorry you lost , the number was ',number)
        break