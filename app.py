#!/usr/bin/python3.9

import GuessGame
import MemoryGame
import CurrencyRouletteGame
global difficulty, decision
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/index.html")
def upload_file():
    return render_template('upload.html')

@app.route("/hello.html")
def hello():
    return render_template('hello.html')


@app.route("/uploader", methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return f'file {f.filename} uploaded successfully'

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
        if 'Guess Game' in request.form:
            game_name = 'Guess Game'
            return render_template('choosedifficulty.html', game_name=game_name)
        if 'Currency Roulette' in request.form:
            game_name = 'Currency Roulette'
            return render_template('choosedifficulty.html', game_name=game_name)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True, template_folder='/app/Templates', static_folder='/app/Static')

