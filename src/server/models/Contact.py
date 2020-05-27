class Contact:
    # initial constructor to set the values
    def __init__(self,contact_id,first,last,year):
        self.contact_id =None 
        self.first = first
        self.last = last
        self.year = year

    def printObj(obj):
        print(obj.contact_id,obj.first,obj.last,obj.year)

Jeff = Contact(None, 'Jeff', 'Cate', 1991)
Jeff.printObj()