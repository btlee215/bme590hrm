from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return "Hello World! %s" % name

@app.route("/data/")
def temptime():
    arr = {"temp": [20, 21, 21],"time":[10,20,30],"unit":"s"}
    return jsonify(arr)

@app.route("/add", methods = ['POST'])
def sum():
    r = request.get_json()
    a = r['a']
    b = r['b']
    sum = a + b
    return '{:d}'.format(sum)

