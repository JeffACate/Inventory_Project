import pyodbc

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
    contact = {
            'id':row[0],
            'first':row[1],
            'last':row[2],
            'year':row[3]
    }
    return contact

def DeleteContact(id):
    cursor.execute(f'DELETE FROM Contacts WHERE id={id}')
    return f'1 contacts deleted'
