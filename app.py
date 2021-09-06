from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Kin DB Server'

if __name__ == '__main__':
    app.run(debug=True)