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
            game_path = 'memorygame'
            return render_template('choosedifficulty.html', game_name=game_name, game_path=game_path)
        if 'Guess_Game' in request.form:
            game_name = 'Guess Game'
            game_path = 'guessgame'
            return render_template('choosedifficulty.html', game_name=game_name, game_path=game_path)
        if 'Currency_Roulette' in request.form:
            game_name = 'Currency Roulette'
            game_path = 'currencyroulette'
            return render_template('choosedifficulty.html', game_name=game_name, game_path=game_path)


@app.route("/currencyroulette", methods=['POST'])
def game_launcher():
    if request.method == 'POST':
        if "1" in request.form:
            difficulty = 1
            CurrencyRouletteGame.play(difficulty)
        if "2" in request.form:
            difficulty = 2
            CurrencyRouletteGame.play(difficulty)
        if "3" in request.form:
            difficulty = 3
            CurrencyRouletteGame.play(difficulty)
        if "4" in request.form:
            difficulty = 4
            CurrencyRouletteGame.play(difficulty)
        if "5" in request.form:
            difficulty = 5
            CurrencyRouletteGame.play(difficulty)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)

