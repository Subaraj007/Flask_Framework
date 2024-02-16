from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')  # Specify the templates folder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')  #  an 'about.html' template

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name) #for user.html template


if __name__ == "__main__":
    app.run(debug=True)