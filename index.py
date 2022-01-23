# Import flask & other utils
from flask import Flask, jsonify, request


# Init flask app
app = Flask(__name__)


# Index route
@app.route('/', methods=['GET'])
def home():
    if(request.method == 'GET'):
        data = "Welcome to Flask REST API"
        return jsonify({'msg': data})
    else:
        return jsonify({"err": "Invalid request method please use GET method"}), 400


# Error handler
@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorCode': 404, 'message': 'Route not found'}), 404


# driver function
if __name__ == '__main__':

    app.run(debug=True, port=5170)