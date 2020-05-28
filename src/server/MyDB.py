import pyodbc
import models.Contact as Models

conn = pyodbc.connect(
    r"Driver={SQL Server};"
    r"Server=DESKTOP-C2482N8\SQLEXPRESS;"
    r"Database=NM_Inventory_App;"
    r"Trusted_Connection=yes;"
)

cursor = conn.cursor()

def GetContacts():
    statement = 'SELECT * FROM Contacts'
    cursor.execute(statement)
    contacts = []
    for row in cursor:
        contacts.append(
            {
            'id':row[0],
            'first':row[1],
            'last':row[2],
            'year':row[3]
            })
    return contacts

def GetContact(id):
    row = cursor.execute(f'SELECT * FROM Contacts WHERE id={id}').fetchone()
    print(row)
    person = Models.Contact(row[0],row[1], row[2],row[3])
    person.printObj()
    return person

def DeleteContact(id):
    response = cursor.execute(f'DELETE FROM Contacts WHERE id={id}')
    print(response)
    conn.commit()
    return {
        'message':f'1 contacts deleted'
        }
