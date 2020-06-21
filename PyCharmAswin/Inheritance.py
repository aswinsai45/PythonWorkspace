from pprint import pprint
#
# print ("Available commands = 'cust details', 'emergency details', 'birth details' and, 'all details'")
# Choice = input ("What do you want to know? ")


# Details of customers

class customer:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def printmyName(self,myName):
        print("Public Method Hello" + myName)
        self.__myAgePrivate("25")

    def __myAgePrivate(self,myAge):
        print ("Private Method My Age is "+ myAge)

    def _myCountry_Protected(self,myCountry):
        print("Protected Method " + myCountry)


# Address Class

class Address (customer):
    def __init__(self,city,state,name, age, height, weight):
        self.city=city
        self.state=state
        super(Address, self).__init__(name, age, "",weight)
        sel

P1 = Address ("kadayanallur","tamilnadu","Suba", "44", "145 cm", "68 kg(s)")
P1.printmyName(" Sai Aswin ")
P1._myCountry_Protected(" India")
P2=customer("Raja", "42", "159 cm", "65 kg(s)")

# P2 = Address ('Kadayam',"Tamil nadu","Raja", "42", "159 cm", "65 kg(s)")
# P3 = Address ("Chennai","TamilNadu","Sai Aswin", "14", "160 cm", "67 kg(s)")
# P4 = Address ("Kdnl","Tamilnadu","Sankarkumar (Siva)", "22", "165 cm", "60 kg(s)")
# P5 = Address ("Avadi","tamil nadu","Sakthivel", "22", "164 cm", "63 kg(s)")

pprint(vars(P1))

print ('\nThank You for using my code.. :)')
