import random
import pytest  
import yaml
import json



def xToY():
    with open('config.yml', 'r') as file:
        import_service = yaml.safe_load(file)
        x = import_service['config_settings']['x']
        y = import_service['config_settings']['y']
    return x,y

def randomCreation(x,y):
    randomnumber = random.randint(x,y)
    return randomnumber

def numberinput():
    while True:
        number = input(f"Pick a number {str(x)} to {str(y)}: ")
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
    guessList = []
    while True:
        guess = int(numberinput())
        guessList.append(guess)
        print("You guessed: ", guess)
        if guess > randomnumber: 
            print("Your guess was too high.")
        elif guess < randomnumber:
            print("Your guess was too low.")
        elif guess == randomnumber:
                break
    return guess, guessList

def answer(guess):
    print("Your guess of",guess,"was correct. Good Job!")

def test_one():
    x,y = xToY()
    assert x < y

def record(filename='log.json'):
    
    with open(filename, "r") as f:
        json_record = json.load(f)
        recordId = json_record['Guessing'][-1]['ID']
        return recordId + 1


def logging(recordId, guess, guessList):
    logginglist = {'ID': recordId,
        'Correct Number': guess,
    'Guesses': len(guessList),
    'GuessList': guessList
    }
    return logginglist

def newfile(filename='log.json'):
    newloginit = {
            "Guessing": [
                { 
                'ID': 0,
                }
                ]
            }
    with open(filename, 'r') as new_file:
        data = new_file.read()
        numchar = len(data)
    if numchar < 1:
        with open(filename, 'w') as new_file:
            json.dump(newloginit, new_file, indent = 3)

def logwriter(logginglist, filename='log.json'):
    with open(filename, 'r') as json_file:
        json_data = json.load(json_file)
    with open(filename, 'w') as json_file:
        json_data["Guessing"].append(logginglist)
        json.dump(json_data, json_file, indent=3)


if __name__ == '__main__':
    x,y = xToY()
    randomnumber = randomCreation(x, y)
    guess, guessList = guessing(randomCreation(x,y))
    answer(guess)
    newfile()
    recordId = record()
    logginglist = logging(recordId, guess, guessList)
    logwriter(logginglist)