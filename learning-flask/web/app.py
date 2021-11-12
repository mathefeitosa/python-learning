from operator import pos
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from personal_utils import error

app = Flask(__name__)

api = Api(app)


def checkPostedData(posted_data, function_name):
  if function_name == 'divide' and posted_data['y'] == 0:
    return error('Cant divide by zero.')
  if 'x' not in posted_data or 'y' not in posted_data:
    return 301
  else:
    return 200


class Add(Resource):
  def post(self):
    # get posted data
    postedData = request.get_json()

    # check if posted data is valid
    if checkPostedData(postedData, 'add') != 200:
      return error('Missing parameters.')

    # getting the parameters
    x = postedData['x']
    y = postedData['y']

    # calculating
    result = int(x)+int(y)

    # returning
    return jsonify({
        'Message': result,
        'Status Code': 200
    })


class Subtract(Resource):
  def post(self):
    # get posted data
    postedData = request.get_json()

    # check if posted data is valid
    if checkPostedData(postedData, 'subtract') != 200:
      return error('Missing parameters.')

    # getting the parameters
    x = postedData['x']
    y = postedData['y']

    # calculating
    result = int(x)-int(y)

    # returning
    return jsonify({
        'Message': result,
        'Status Code': 200
    })


class Multiply(Resource):
  def post(self):
    # get posted data
    postedData = request.get_json()

    # check if posted data is valid
    if checkPostedData(postedData, 'multiply') != 200:
      return error('Missing parameters.')

    # getting the parameters
    x = postedData['x']
    y = postedData['y']

    # calculating
    result = int(x)*int(y)

    # returning
    return jsonify({
        'Message': result,
        'Status Code': 200
    })


class Divide(Resource):
  def post(self):
    # get posted data
    postedData = request.get_json()

    # check if posted data is valid
    if checkPostedData(postedData, 'divide') != 200:
      return error('Missing parameters.')

    # getting the parameters
    x = postedData['x']
    y = postedData['y']

    # calculating
    result = int(x)/int(y)

    # returning
    return jsonify({
        'Message': result,
        'Status Code': 200
    })


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Divide, '/divide')
api.add_resource(Multiply, '/multiply')

if __name__ == "__main__":
  app.run(debug=True)
