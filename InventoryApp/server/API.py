import flask 
from flask import request, jsonify, redirect, render_template
from MyDB import QueryDB

# SET UP FLASK APP
# SET UP DEBUGGER
app = flask.Flask(__name__)
app.config["DEBUG"] = True 

#get data
#contacts = QueryDB('SELECT * FROM Contacts')

#  [
#         {
#             'id': 0,
#             'firstName': 'Jeff',
#             'lastName': 'Cate',
#             'birthYear': 1991
#         },
#         {
#             'id': 1,
#             'firstName': 'Alisha',
#             'lastName': 'Luymes',
#             'birthYear': 1991
#         },
#         {
#             'id': 2,
#             'firstName': 'Colleen',
#             'lastName': 'Cate',
#             'birthYear': 1993
#         }
#     ]



# GET: HELLO WORLD STRING
@app.route('/', methods=['GET'])
def home():
    return '''<h1>ERROR 404: KNOWLEDGE NOT FOUND<br>working on REDIRECTING to a page: /client/index.html</h1>
    # return render_template('/client/index.html')
    '''

# GET: ALL CONTACTS
@app.route('/api/contacts/all', methods=['GET'])
def GetAllContacts():
    statement = 'SELECT * FROM Contacts'
    contacts = QueryDB(statement)
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
    statement = (f'SELECT * FROM Contacts WHERE id={id}')
    contact = QueryDB(statement)

    return jsonify(contact)

app.run()
