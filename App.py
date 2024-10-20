@app.route('/multiply/<int:numberA>/<int:numberB>', methods=['GET'])
def multiply(numberA, numberB):
    result = numberA * numberB
    return jsonify(status=200, result=result)

@app.route('/mod/<int:numberA>/<int:numberB>', methods=['GET'])
def mod(numberA, numberB):
    result = numberA % numberB
    return jsonify(status=200, result=result)