from flask import Flask, request, jsonify, redirect, render_template
from flask_cors import CORS
import MyDB
from MyDB import Contact_Model

# SET UP FLASK APP
# SET UP DEBUGGER
app = Flask(__name__)
app.config["DEBUG"] = True 
CORS(app)

# GET: HELLO WORLD STRING
@app.route('/', methods=['GET'])
def home():
    return '''
    <html style="background-color: blue; color: yellow;">
        <div>
            <h1 style="text-align: center;">Api / Page</h1>
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

# POST: CREATE - ?first=<string>&last=<string>&year=<int>
@app.route('/api/contacts/create', methods=['GET'])
def CreateContact():
    results = MyDB.CreateContact(request.args['first'],request.args['last'],int(request.args['year']))
    return jsonify(results)

app.run()