import pyodbc

conn = pyodbc.connect(
    r"Driver={SQL Server};"
    r"Server=DESKTOP-C2482N8\SQLEXPRESS;"
    r"Database=NM_Inventory_App;"
    r"Trusted_Connection=yes;"
)

cursor = conn.cursor()

def QueryDB(statement):
    cursor = conn.cursor()
    print('funtion executed.')
    cursor.execute(statement)
    contacts = []
    for row in cursor:
        id = row[0]
        first = row[1]
        last = row[2]
        year = row[3]
        contacts.append(
            {
            'id':id,
            'first':first,
            'last':last,
            'year':year
            })
        print(f'   id = {id}\nfirst = {first}\n last = {last}\n year = {year}\n')
    return contacts
        

people = QueryDB('SELECT * FROM Contacts')
for person in people:
    print(person['id'],person['first'],person['last'],person['year'])
cursor.close()

