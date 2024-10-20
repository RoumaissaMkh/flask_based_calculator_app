
@app.route('/divide/<int:numberA>/<int:numberB>', methods=['GET'])
def divide(numberA, numberB):
    if numberB == 0:
        return jsonify(status=400, result='Division by zero error')
    result = numberA / numberB
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

