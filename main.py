from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return 'Start page'


@app.route('/profile')
def profile():
    return 'Profile page'


if __name__ == '__main__':
    app.run(debug=True)
