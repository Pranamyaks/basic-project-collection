import random
secrete_number=random.randint(1,100)
attempts=0
print("Welcome to guess the number game!!")
print("i have selected number between 1 and 100")
guess=0
while guess!=secrete_number:
    guess=int(input("Enter your guess:"))
    attempts+=1
    if guess<secrete_number:
        print("sorry!guess is too low..")
    elif guess>secrete_number:
        print("sorry!guess is too high..")
print("congrats!! your guess is correct..")  
print(f'you guessed number in the attempt of {attempts}')          
