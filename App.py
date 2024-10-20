@app.route('/add/<int:numberA>/<int:numberB>', methods=['GET'])
def add(numberA, numberB):
    result = numberA + numberB
    return jsonify(status=200, result=result)

@app.route('/minus/<int:numberA>/<int:numberB>', methods=['GET'])
