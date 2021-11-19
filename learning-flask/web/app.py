"""
-> Registration of users
-> Each user gets 10 tokens
-> Store a sentence on our database for 1 token
-> Retrieve his stored sentence for 1 token
-> Password and username storage
"""
from logging import error
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt


app = Flask(__name__)
api = Api(app)

# the 'db'is the same of docker-composer
client = MongoClient("mongodb://hidden-everglades-51006.herokuapp.com:27017")
db = client.SentencesDatabase
users = db['users']


class Register(Resource):
  def post(self):
    # get posted data
    posted_data = request.get_json()

    # check if the parameters exits
    if 'username' not in posted_data or 'password' not in posted_data:
      return jsonify({'message': 'Incorrect parameters.'})

    # getting the data
    username = posted_data['username']
    password = posted_data['password']

    # generating password -> hash(password+salt)
    hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    # store username and hash in the database
    users.insert_one({
        "username": username,
        'password': hashed_password,
        'sentence': "",
        'tokens': 6
    })

    # returning the status
    return jsonify({
        'status': 200,
        'message': 'You successfully signed up for the API'
    })


def verify(username, password):
  hashed_password = users.find({
      'username': username,
  })[0]['password']

  if bcrypt.hashpw(password.encode('utf8'), hashed_password) == hashed_password:
    return True
  else:
    return False


def countTokens(username):
  tokens = users.find({
      'username': username
  })[0]['tokens']
  return tokens


class Store(Resource):
  def post(self):
    # getting the posted data
    posted_data = request.get_json()

    # reading the data
    username = posted_data['username']
    password = posted_data['password']
    sentence = posted_data['sentence']

    # verify if the username and password match
    is_pw_correct = verify(username, password)
    if not is_pw_correct:
      return jsonify({
          'status': 302,
          'message': 'Username and password doesnt match.'
      })

    # verify if the user has enough tokens
    tokens = countTokens(username)
    if tokens <= 0:
      return jsonify({
          'status': 301,
          'message': 'You dont have enough tokens.'
      })

    # store the sentence, take one token away and return 200 OK
    users.update(
        {'username': username},
        {'$set': {
            "sentence": sentence,
            "tokens": tokens-1
        },
        }
    )
    return jsonify({
        'status': 302,
        'message': 'Sentence saved successfully.'
    })


class Get(Resource):
  def post(self):
    posted_data = request.get_json()

    username = posted_data['username']
    password = posted_data['password']

    if not verify(username, password):
      return jsonify({
          "status": 302,
          "message": "Password and username dont match!"
      })
    # getting the sentence
    sentence = users.find({'username': username})[0]['sentence']
    tokens = countTokens(username)
    users.update(
        {'username': username},
        {'$set': {
            "tokens": tokens-1
        },
        }
    )

    return jsonify({
        'status': 200,
        'message': sentence
    })


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Get, '/get')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)


"""
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
