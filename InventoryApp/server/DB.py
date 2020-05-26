import pyodbc

conn = pyodbc.connect(
    r"Driver={SQL Server};"
    r"Server=DESKTOP-C2482N8\SQLEXPRESS;"
    r"Database=NM_Inventory_App;"
    r"Trusted_Connection=yes;"
)

cursor = conn.cursor()



def this(statement):
    print('funtion executed.')
    cursor.execute(statement)
    for row in cursor:
        id = row[0]
        first = row[1]
        last = row[2]
        year = row[3]
        print(f'   id = {id}\nfirst = {first}\n last = {last}\n year = {year}\n')
        if first == 'Jeff':
            print("Jeff was found\n\n")
        else:
            print('Jeff was not found!\n\n')

this('SELECT * FROM Contacts')

cursor.close()

