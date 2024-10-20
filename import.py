from flask import Flask, jsonify

app = Flask(name)

if name == 'main':
    app.run(debug=True)
