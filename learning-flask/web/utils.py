from flask.json import jsonify


def json_error(message):
  return jsonify({
      'message': message
  })
