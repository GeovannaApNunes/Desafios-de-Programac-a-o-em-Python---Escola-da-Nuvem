myString = "Isso é uma string."
print(myString)
print(type(myString))

myString = "Isso é uma string"
print(myString)
print(type(myString))
print(myString + ", ela é do tipo de dados " + str(type(myString)))

primeiraString = "Geovanna "
segundaString = "Nunes"
terceiraString = primeiraString + segundaString
print(terceiraString)

name = input("What is your name? ")
print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a color {} and aniaml {}!".format(name,color,animal))