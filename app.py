from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello qweqweqw, {escape(name)}!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
