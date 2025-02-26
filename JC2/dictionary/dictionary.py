dictionary = {"England":"London",
              "France":"Paris",
              "Germany":"Berlin"}

dictionary["Indonesia"] = "Jakarta" #this definition will be added
dictionary["England"] = "Wales" #initial London get overwritten by Wales

#search for key
key = input("Input a key: ")
if key in dictionary:
    print(dictionary[key])
else:
    print("Not Found")

#print the entire dictionary
print(dictionary)

#clear the dictionary
dictionary.clear() #its a function
print(dictionary)



