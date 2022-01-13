import random

def xToY():
    x = 4
    y = 3
    if x >= y:
        print("Please make sure X is the low number.")
        quit()
    return x,y

def randomCreation(x,y):
    randomnumber = random.randint(x,y)
    return randomnumber

def numberinput():
    while True:
        number = input("Pick a number {} to {}: ".format(str(x),str(y)))
        try:
            val = int(number)
            if val < 1:
                print("Sorry, input must be a positive integer, try again")
                continue
            break
        except ValueError:
            print("That's not an int!")
    return number

def guessing(randomnumber):
    while True:
        guess = int(numberinput())
        print("You guessed: ", guess)
        if guess > randomnumber: 
            print("Your guess was too high.")
        elif guess < randomnumber:
            print("Your guess was too low.")
        elif guess == randomnumber:
                break
    return guess

def answer(guess):
    print("Your guess of",guess,"was correct. Good Job!")

if __name__ == '__main__':
    x,y = xToY()
    answer(guessing(randomCreation(x,y)))