"""
-> Registration of users
-> Each user gets 10 tokens
-> Store a sentence on our database for 1 token
-> Retrieve his stored sentence for 1 token
-> Password and username storage
"""


"""from operator import pos
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

# the 'db'is the same of docker-composer
client = MongoClient("mongodb://db:27017")
db = client['UserNum']
visit_counter = db['visit_counter']

visit_counter.insert_one({
    'num_of_users': 0
})


class Visit(Resource):
  def get(self):
    previous_num = visit_counter.find()[0]['num_of_users']
    new_num = int(previous_num)+1
    visit_counter.update({}, {'$set': {'num_of_users': new_num}})
    return 'Hello user ' + str(new_num)
# -------------------------------------------------------------------------------
# PERSONAL UTILS


def error(message):
  return jsonify({
      "error": message
  })
# -------------------------------------------------------------------------------


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
api.add_resource(Visit, '/hello')


if __name__ == "__main__":
  app.run(host='0.0.0.0')
"""
