from flask import Flask, request, render_template, json

app = Flask(__name__)

@app.route('/')
def hello():
    name = "World"
    return 'Hello , {}!'.format(name)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/ledOn')
def ledOn():
    from controllers import lightsController
    lightsController.turnOnBoardLed()
    return json.dumps({'Led is on':True}), 200, {'ContentType':'application/json'} 

@app.route('/ledOff')
def ledOff():
    from controllers import lightsController
    lightsController.turnOffBoardLed()
    return json.dumps({'Led is on':False}), 200, {'ContentType':'application/json'} 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5001"), debug=True)


