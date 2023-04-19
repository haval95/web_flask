from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "webiste content"
@app.route('/contact')
def contact():
    return "webiste contact page"

if __name__ == '__main__':
    app.run(debug=True)
