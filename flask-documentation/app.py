from os import error
from flask import Flask, jsonify, request

from personal_utils import error

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hellooooo!'


@app.route('/add_two_nums', methods=['POST'])
def add_two_nums():
  dataDict = request.get_json()

  # veirifying existance of data
  if 'operator' not in dataDict:
    return error('There is no operator in the request.'), 301
  if 'x' not in dataDict:
    return error('Missing X parameter.'), 301
  elif 'y' not in dataDict:
    return error('Missing Y parameter.'), 301

  # collecting data
  x = dataDict['x']
  y = dataDict['y']
  op = dataDict['operator']
  if op == 'sum':
    return jsonify({
        'result': x+y
    }), 200
  elif op == 'multiply':
    return jsonify({
        'result': x*y
    }), 200
  elif op == 'subtract':
    return jsonify({
        'result': x-y
    }), 200
  elif op == 'divide':
    if y is not 0:
      return jsonify({
          'result': x/y
      }), 200
    else:
      return error("Can't divide by zero."), 302
  else:
    return error('Operation not suported.'), 302


if __name__ == "__main__":
  app.run(debug=True)
