from flask import jsonify


def error(message):
  return jsonify({
      "error": message
  })
