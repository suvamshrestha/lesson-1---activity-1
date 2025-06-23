import random
playing = True
number = str(random.randint(0,5))
print("Welcome to the Number Game!")
print("i will generate a number from 0 - 9")
print("if you will 1 time, you will win")
while playing:
    guess = input("enter your guess: ")
    if number == guess:
        print("you win")
        print("the number was", number)
        break
    else:
        print("you lose")
        print("the number was", number)
        print("try again")