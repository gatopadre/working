from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = "World"
    return 'Hello , {}!'.format(name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5001"), debug=True)

