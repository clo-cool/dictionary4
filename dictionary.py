# creating a dictionary

fruit = ["apple","sdfgh","banana"]
age = [59,6,37,1234567890]

#creating address dictionary

address = {
    "name":"aisling",
    "home":"castlegragry",
    "socity":"xyz",
    "city":"new york",
    "country":"USA"
}
print(address)
#printing individual item from are dictionary
print(address["socity"])
print(address["country"])
print(address["name"])

#how to get all the keys of the dictionary
print(address.keys())

#how to get all the values of the dictionary
print(address.values())

#using for loop for printing each dictionary data one by one
for key in address.keys():
    print(key,address[key])

#check if a key exist in a dictionary
if "state" in address:
    print("Yes key is there.")

else:
    print("No it is not there.Sorry")

#adding a key and value pair 
address["job"] = "swimmer"
print(address)

# changing a value of key that is already there.
address["job"] = "scientist"
print(address)
#how to delet
del(address["country"])
print(address)


