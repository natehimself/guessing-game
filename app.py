from flask import Flask, render_template, request, jsonify
import guess as your_script # Replace with the actual name of your script file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess2', methods=['POST'])
def guess2():
    x, y = your_script.xToY()
    max_guess = your_script.max_guesses()
    randomnumber = your_script.randomCreation(x, y)

    guess, guessList, i = your_script.guessing(randomnumber, 1)
    your_script.answer(guess, i, max_guess, randomnumber)

    recordId = your_script.record()
    logginglist = your_script.logging(recordId, guessList, max_guess, randomnumber, x, y)
    your_script.logwriter(logginglist)

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
