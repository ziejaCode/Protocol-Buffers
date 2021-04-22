import addressbook_pb2 as addressbook_pb2


addressYellowBook = addressbook_pb2.AddressBook()

addressYellowBook.people.add(name="marian kovalczyk", id=234, email="mafsra@gnail.com")


#franekD = addressbook_pb2.Person()
franekD = addressYellowBook.people.add()

franekD.name="franek Dolas"
franekD.id=3434
franekD.email="frade@fgeewe"

franekPhone = franekD.phones.add()
franekPhone.number = "2345453442342"
franekPhone.type = franekD.WORK

# extend list of phones for another phone
def extendPhones(num, typ):
    franekPhone2 = addressbook_pb2.Person().PhoneNumber()
    franekPhone2.number = num
    if typ == "HOME":
        franekPhone2.type = franekD.HOME
    else:
        franekPhone2.type = franekD.WORK

    franekD.phones.extend([franekPhone2])


extendPhones("234234123", "WORK")

# how to extend result list for one more existing Persong (element)
robZ = addressbook_pb2.Person()
robZ.name ="Robert Zych"
robZ.id = 2236
robZ.email = "robz@gnail"
addressYellowBook.people.extend([robZ])





#print(franekD)

print(addressYellowBook)



