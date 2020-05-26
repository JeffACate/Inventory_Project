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
@app.route('/api/contacts/all', methods=['GET'])
def GetAllContacts():
    return jsonify(contacts)

# GET: BY ID
@app.route('/api/contacts', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    print(request.args['id'])
    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for contact in contacts:
        if contact['id'] == id:
            results.append(contact)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
