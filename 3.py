MyString= "This is a string"
print(MyString)
print(type(MyString))
print(MyString + " is of the data type"+ str(type(MyString)))

firststring="water"
secondstring="fall"
thirdstring= firststring+secondstring
print(thirdstring)

name=input("what is your name?")
print(name)
color=input("what is your favorite color?")
animal=input("what is your favorite animal?")
print("{}, you like a {} {}!".format(name,color,animal))