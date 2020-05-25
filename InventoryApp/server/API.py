import flask 
from flask import request, jsonify, redirect, render_template

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



# GET: HELLO WORLD STRING
@app.route('/', methods=['GET'])
def home():
    return '''<h1>ERROR 404: KNOWLEDGE NOT FOUND<br>working on REDIRECTING to a page: /client/index.html</h1>
    # return render_template('/client/index.html')
    '''

# GET: ALL CONTACTS
@app.route('/contacts/all', methods=['GET'])
def GetAllContacts():
    return jsonify(contacts)

# GET: BY ID
@app.route('/contacts/', methods=['GET'])
def GetContact():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No id field provided. Please choose and id.'
    
    results = []

    for contact in contacts:
        if contact['id'] == id:
            results.append(contact)

    return jsonify(results)

app.run()
