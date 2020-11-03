from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/tasks')
def tasks():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/repl_one')
def repl_one():
    return render_template('repl_one.html')

if __name__ == '__main__':
    app.run(debug=True, port='4000')