from pprint import pprint

print ("Available commands = 'cust details', 'emergency details', 'birth details' and, 'all details'")
Choice = input ("What do you want to know? ")


# Details of customers

class customer:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


P1 = customer ("Suba", "44", "145 cm", "68 kg(s)")
P2 = customer ("Raja", "42", "159 cm", "65 kg(s)")
P3 = customer ("Sai Aswin", "14", "160 cm", "67 kg(s)")
P4 = customer ("Sankarkumar (Siva)", "22", "165 cm", "60 kg(s)")
P5 = customer ("Sakthivel", "22", "164 cm", "63 kg(s)")


# In Case of Emergency

class EmergencyDetails:
    def __init__(self, name, emerphone, idno, insprovider):
        self.name = name
        self.emerphone = emerphone
        self.idno = idno
        self.insprovider = insprovider


# ed = Emergency Details

ed1 = EmergencyDetails ("Raja", "917652543", "561072", "ICICI Prudential")
ed2 = EmergencyDetails ("Suba", "7397394410", "763975", "Star Health Insurance Policies")
ed3 = EmergencyDetails ("Sai Aswin", "9952995638", "10763", "Star Health Insurance Policies")
ed4 = EmergencyDetails ("Sankarkumar", "9698120968", "753697", "Star Health Insurance Policies")
ed5 = EmergencyDetails ("Sakthivel", "9962680103", "10763", "Star Health Insurance Policies")


# Place of Birth

class POB:
    def __init__(self, name, nameofpob, district, state):
        self.name = name
        self.nameofpob = nameofpob
        self.district = district
        self.state = state


bd1 = POB (">>Raja", "Kadayam", "Tirunelveli", "Tamil Nadu")
bd2 = POB (">>Suba", "Kadayanallur", "Tirunelveli", "Tamil Nadu")
bd3 = POB (">>Sai Aswin", "Kadayanallur", "Tirunelveli", "Tamil Nadu")
bd4 = POB (">>Sankarkumar", "Kadayanallur", "Tirunelveli", "Tamil Nadu")
bd5 = POB (">>Sakthivel", "Kadayanallur", "Tirunelveli", "Tamil Nadu")

if Choice == "cust details":
    pprint (vars (P1))
    pprint (vars (P2))
    pprint (vars (P3))
    pprint (vars (P4))
    pprint (vars (P5))


elif Choice == "emergency details":
    pprint (vars (ed1))
    pprint (vars (ed2))
    pprint (vars (ed3))
    pprint (vars (ed4))
    pprint (vars (ed5))

elif Choice == "birth details":
    pprint (vars (bd1))
    pprint (vars (bd2))
    pprint (vars (bd3))
    pprint (vars (bd4))
    pprint (vars (bd5))

elif Choice == "all details":
    pprint (vars (P1))
    pprint (vars (P2))
    pprint (vars (P3))
    pprint (vars (P4))
    pprint (vars (P5))

    pprint (vars (ed1))
    pprint (vars (ed2))
    pprint (vars (ed3))
    pprint (vars (ed4))
    pprint (vars (ed5))

    pprint (vars (bd1))
    pprint (vars (bd2))
    pprint (vars (bd3))
    pprint (vars (bd4))
    pprint (vars (bd5))

print ('\nThank You for using my code.. :)')
