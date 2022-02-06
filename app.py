from flask import Flask, redirect, request, url_for, render_template
from sudoku_game import SudokuGenerator
from sudoku import sudoku
from forms import indexForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    index_form = indexForm(csrf_enabled=False)
    if request.method == 'POST':
        if index_form.validate_on_submit():
            name = index_form.name.data
            city = index_form.city.data
            phrase = index_form.phrase.data
            return redirect(url_for("play", name=name, city=city, phrase=phrase, _external=True, _schema='https'))
    return render_template("index.html", template_form=index_form)

@app.route('/play', methods=['GET', 'POST'])
def play():
    return render_template("play.html")

@app.route('/win', methods=['GET', 'POST'])
def win():
    return render_template("win.html")

@app.route('/lose', methods=['GET', 'POST'])
def lose():
    return render_template("lose.html")