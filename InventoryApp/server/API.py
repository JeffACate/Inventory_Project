import flask
from flask import request, jsonify

# SET UP FLASK APP
# SET UP DEBUGGER
app = flask.Flask(__name__)
app.config["DEBUG"] = True 

# TEST DATA
contacts = [
    {
        'id': 0,
        'firstName': 'Jeff',
        'lastName': 'Cate',
        'birthYear': 1991
    },
    {
        'id': 1,
        'firstName': 'Alisha',
        'lastName': 'Luymes',
        'birthYear': 1991
    },
    {
        'id': 2,
        'firstName': 'Colleen',
        'lastName': 'Cate',
        'birthYear': 1993
    }
]




@app.route('/', methods=['GET'])
def home():
    return "<h1>hello world</h1>"

@app.route('/', methods=['GET'])
def GetAll():
    return jsonify(contacts)

app.run()
