from flask import Flask, redirect, request, url_for, render_template
from sudoku_game import SudokuGenerator
from forms import indexForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    index_form = indexForm()
    if request.method == 'POST':
        if index_form.validate_on_submit():
            name = index_form.name.data
            city = index_form.city.data
            phrase = index_form.phrase.data
            return redirect(url_for("play", name=name, city=city, phrase=phrase))
    return render_template("index.html", template_form=index_form)

@app.route('/play')
def play():
    return url_for(render_template("play"))

@app.route('/win')
def win():
    return "Game"

@app.route('/lose')
def lose():
    return "Game"