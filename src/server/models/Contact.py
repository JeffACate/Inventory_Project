class Contact:
    # initial constructor to set the values
    def __init__(self,contact_id,first,last,year):
        self.contact_id = None 
        self.first = first
        self.last = last
        self.year = year

    # A way to print the object variables fancy like.
    def printObj(obj):
        print(obj.contact_id,obj.first,obj.last,obj.year)

    def MakeContact(first,last,year):
        contact = Contact(None,first,last,year)
        return contact
    
    def MakeContact(id,first,last,year):
        contact = Contact(id,first,last,year)
        return contact

