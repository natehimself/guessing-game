from flask import Flask, render_template, request, jsonify
import guess as g # Replace with the actual name of your script file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess2', methods=['POST'])
def guess2():
    x, y = g.xToY()
    max_guess = g.max_guesses()
    randomnumber = g.randomCreation(x, y)

    guess, guessList, i = g.guessing(randomnumber, 1)
    g.answer(guess, i, max_guess, randomnumber)

    recordId = g.record()
    logginglist = g.logging(recordId, guessList, max_guess, randomnumber, x, y)
    g.logwriter(logginglist)

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
