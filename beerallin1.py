class Beer:
    def __init__(self, id, name, type, manufacturer, ibu):
        self.id = id
        self.name = name
        self.type = type
        self.manufacturer = manufacturer
        self.ibu = ibu 
    
    def isHoppy (self):
        if self.ibu > 50:
            print(f"t or f - {self.name} is a hoppy beer: \ntrue")
        else:
            print(f"t or f - {self.name} is a hoppy beer: \nfalse")

Coors = {'Id' : 1, 'Name' : 'Coors', 'Type' : 'Lager', 'Manufacturer' :'Molson Coors', 'Ibu' : 15,}
Avery = {'Id' : 2,'Name' : 'Avery IPA', 'Type' : 'American IPA', 'Manufacturer' : 'Avery', 'Ibu' : 69,}

bier1 = Beer(Coors['Id'], Coors['Name'], Coors['Type'], Coors['Manufacturer'], Coors['Ibu'])
bier1.isHoppy()

bier2 = Beer(Avery['Id'], Avery['Name'], Avery['Type'], Avery['Manufacturer'], Avery['Ibu'])
bier2.isHoppy()

