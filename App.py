from flask import Flask, jsonify
app = Flask(name)

@app.route('/add/<int:numberA>/<int:numberB>', methods=['GET'])
def add(numberA, numberB):
    result = numberA + numberB
    return jsonify(status=200, result=result)

@app.route('/minus/<int:numberA>/<int:numberB>', methods=['GET'])
def minus(numberA, numberB):
    result = numberA - numberB
    return jsonify(status=200, result=result)

@app.route('/multiply/<int:numberA>/<int:numberB>', methods=['GET'])
def multiply(numberA, numberB):
    result = numberA * numberB
    return jsonify(status=200, result=result)

@app.route('/mod/<int:numberA>/<int:numberB>', methods=['GET'])
def mod(numberA, numberB):
    result = numberA % numberB
    return jsonify(status=200, result=result)

if name == 'main':
    app.run(debug=True)

