import random 
import yaml
import json

def xToY(): #Reads YAML file with config information.
    with open('config.yml', 'r') as file:
        import_service = yaml.safe_load(file)
        x = import_service['config_settings']['x']
        y = import_service['config_settings']['y']
    return x,y

def max_guesses(): #Reads YAML file with config information.
    with open('config.yml', 'r') as file:
        import_service = yaml.safe_load(file)
        max_guess = import_service['config_settings']['max_guess']
    return max_guess

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

def guessing(randomnumber, i): #Checks if random number is correct.
    guessList = []
    while i < int(max_guesses())+1:
        guess = int(numberinput())
        guessList.append(guess)
        print("You guessed: ", guess)
        if guess < x:
            print("Your guess is out of bounds, Guess again")
        elif guess > y:
            print("Your guess is out of bounds, Guess again")
        elif guess > randomnumber: 
            print("Your guess was too high.")
            i += 1
        elif guess < randomnumber:
            print("Your guess was too low.")
            i += 1
        elif guess == randomnumber:
                break     
    return guess, guessList, i

def answer(guess, i, max_guess, randomnumber): #Good job.
    while True:
        if int(max_guess)+1 == i:
            print("Sorry you guessed to many times. The correct number was",randomnumber)
            break
        else: 
            print("Your guess of",guess,"was correct. Good Job!")
            break

def newfile(filename='log.json'): #Creates and initializes a JSON file to capture guess logs.
    newloginit = {"Guessing":[{'ID': 0,'Correct Number': 0,'RangeX': 0,'RangeY': 0,'Guesses': 0,'Max Guesses': 0,'GuessList': 0}]}
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

def logging(recordId, guessList, max_guess, randomnumber, x, y): #Creates JSON attribute-value pairs.
    logginglist = {'ID': recordId,'Correct Number': randomnumber,'RangeX': x,'RangeY': y,'Guesses': len(guessList),'Max Guesses': max_guess,'GuessList': guessList}
    return logginglist

def logwriter(logginglist, filename='log.json'): #Logs varius data points, formats JSON file.
    with open(filename, 'r') as json_file:
        json_data = json.load(json_file)
    with open(filename, 'w') as json_file:
        json_data["Guessing"].append(logginglist)
        json.dump(json_data, json_file, indent=3)

if __name__ == '__main__': #Takes X,Y and creates a random number. Checks the random number against the gusses and then passes all the information onto the logs. 
    x,y = xToY() 
    i=1
    randomnumber = randomCreation(x, y)
    guess, guessList, i = guessing(randomnumber, i)
    max_guess = max_guesses()
    answer(guess, i, max_guess, randomnumber)
    newfile()
    recordId = record()
    logginglist = logging(recordId, guessList, max_guess, randomnumber, x, y)
    logwriter(logginglist)