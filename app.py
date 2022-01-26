# Import flask & other utils
from flask import Flask, jsonify, request
from pymongo import MongoClient
from decouple import config

# Init flask app
app = Flask(__name__)

DB_USER = config('DB_USERNAME')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config("DB_NAME")
DB_NAME_COL = config("DB_NAME_COL")


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://"+DB_USER+":" + \
        DB_PASSWORD+"@"+DB_NAME+".mongodb.net/"+DB_NAME_COL

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClients
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client


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

    dbname = get_database()
    app.run(debug=True, port=5170)
