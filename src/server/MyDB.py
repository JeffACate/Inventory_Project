import pyodbc
import models.Contact as Models
import json 

Contact_Model = {
    'id' : 'id',
    'first' : 'First_Name',
    'last' : 'Last_Name',
    'year' : 'Birth_Year'
}

conn = pyodbc.connect(
    r"Driver={SQL Server};"
    r"Server=DESKTOP-C2482N8\SQLEXPRESS;"
    r"Database=NM_Inventory_App;"
    r"Trusted_Connection=yes;"
    
)

cursor = conn.cursor()

def GetContacts():
    query = 'SELECT * FROM Contacts'
    cursor.execute(query)
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
    #person = Models.Contact(row[0],row[1], row[2],row[3])
    #personprintObj()
    contact = {
            'id':row[0],
            'first':row[1],
            'last':row[2],
            'year':row[3]
    }
    return contact
#INCOMPLETE
def DeleteContact(id):
    cursor.execute(f'DELETE FROM Contacts WHERE id={id}')
    conn.commit()
    return {
        'message':f'1 contacts deleted'
        }

def CreateContact(first, last, year):
    query = f'''
                INSERT INTO dbo.Contacts (First_Name, Last_Name, Birth_Year)
                VALUES
                ('{first}','{last}',{year})
                '''

    cursor.execute(query)
    conn.commit()
    contact = {
            'first': first,
            'last': last,
            'year': year,
            'message': 'Contact successfullly created'
    }
    return contact


