import random
import pytest  
import yaml
import json

def xToY(): #Reads YAML file with config information.
    with open('config.yml', 'r') as file:
        import_service = yaml.safe_load(file)
        x = import_service['config_settings']['x']
        y = import_service['config_settings']['y']
    return x,y

def randomCreation(x,y): #generates random number between X and Y.
    randomnumber = random.randint(x,y)
    return randomnumber

def numberinput(): #Takes number input and sanitizes it.
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

def guessing(randomnumber): #Checks if random number is correct.
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

def answer(guess): #Good job.
    print("Your guess of",guess,"was correct. Good Job!")

def test_one(): # Pytest function to check if y is greater then x.
    x,y = xToY()
    assert x < y

def newfile(filename='log.json'): #Creates and initializes a JSON file to capture guess logs.
    newloginit = {"Guessing":[{'ID': 0,}]}
    try: 
        open(filename, 'r')
    except FileNotFoundError:
        with open(filename, 'w') as new_file:
            json.dump(newloginit, new_file, indent = 3)
   
def record(filename='log.json'): #Logging function to increment guess IDs in JSON file.
    with open(filename, "r") as f:
        json_record = json.load(f)
        recordId = json_record['Guessing'][-1]['ID']
        return recordId + 1

def logging(recordId, guess, guessList): #Creates JSON attribute-value pairs.
    logginglist = {'ID': recordId,'Correct Number': guess,'Guesses': len(guessList),'GuessList': guessList}
    return logginglist

def logwriter(logginglist, filename='log.json'): #Logs varius data points, formats JSON file.
    with open(filename, 'r') as json_file:
        json_data = json.load(json_file)
    with open(filename, 'w') as json_file:
        json_data["Guessing"].append(logginglist)
        json.dump(json_data, json_file, indent=3)

if __name__ == '__main__': #Takes X,Y and creates a random number. Checks the random number against the gusses and then passes all the information onto the logs. 
    x,y = xToY()
    randomnumber = randomCreation(x, y)
    guess, guessList = guessing(randomCreation(x,y))
    answer(guess)
    newfile()
    recordId = record()
    logginglist = logging(recordId, guess, guessList)
    logwriter(logginglist)