#!/usr/bin/python3.9

import GuessGame
import MemoryGame
import CurrencyRouletteGame

global difficulty, decision
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello():

    return render_template('hello.html')


@app.route("/choose", methods=['POST'])
def game_chooser():
    if request.method == 'POST':
        if request.form['username'] != "":
            name = request.form['username']
            return render_template('ChooseApplication.html', name=name)
        else:
            return render_template('hello.html')

@app.route("/choosedifficulty", methods=['POST'])
def difficulty_chooser():
    if request.method == 'POST':
        if 'Memory_Game' in request.form:
            game_name = 'Memory Game'
            return render_template('choosedifficulty.html', game_name=game_name)
        if 'Guess_Game' in request.form:
            game_name = 'Guess Game'
            return render_template('choosedifficulty.html', game_name=game_name)
        if 'Currency_Roulette' in request.form:
            game_name = 'Currency Roulette'
            return render_template('choosedifficulty.html', game_name=game_name)
@app.route("/guess", method=['POST']
    if request.method == 'POST':
        if
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)

