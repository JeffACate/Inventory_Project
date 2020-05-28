import flask 
from flask import request, jsonify, redirect, render_template
import MyDB

# SET UP FLASK APP
# SET UP DEBUGGER
app = flask.Flask(__name__)
app.config["DEBUG"] = True 

# GET: HELLO WORLD STRING
@app.route('/', methods=['GET'])
def home():
    return '''
    <html style="background-color: blue; color: yellow;">
        <div>
            <h1 style="text-align: center;">Application Home Page</h1>
        </div>
    <html>
    '''

# GET: ALL CONTACTS
@app.route('/api/contacts/all', methods=['GET'])
def GetAllContacts():
    contacts = MyDB.GetContacts()
    return jsonify(contacts)

# GET: BY ID
@app.route('/api/contacts', methods=['GET'])
def GetContactById():
    # VERIFY id EXISTS
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # CALL DB AND QUERY FOR 
    contact = MyDB.GetContact(id)
    # RETURN JSON
    return jsonify(contact)

# POST: DELETE
@app.route('/api/contacts/delete', methods=['GET'])
def DeleteContact():
    # VERIFY id EXISTS
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # CALL DB AND QUERY FOR 
    message = MyDB.DeleteContact(id) 
    # RETURN JSON
    return jsonify(message)

# @app.route('api/contacts/create', methods=['POST'])
''' def CreateContact():
    if 'first' in request.args and 'last' in request.args and 'year' in request.args:
        if request.args['first'] not None and request.args['last'] not None and request.args['year'] not None:
'''

app.run()