import random
system=random.randint(0, 20)
user=-1
guess=0
while system!=user:
    user=int(input('Guess a number between 0 and 20  :'))
    if system==user:
        print('well done')
    elif system>user:
        print('above')
    else:
        print('lower')
    guess += 1
print('Number of digits you guessed  :'+str(guess))


