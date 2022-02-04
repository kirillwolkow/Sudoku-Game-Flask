from flask import Flask


app = Flask(__name__)

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'fjl346lw3SG3tST'
    app.run(debug=True)

@app.route('/')
def index():
    return "<h1>Welcome to the Flask Sudoku Game</h1>"
