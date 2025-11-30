#create class
class Dog:

    #class attribute
    species ="bird"

    #instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age

#instanitiate the Parrot class
blu = Dog("Blu",10)
woo = Dog("Woo",15)

#access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))


#access the instance attributes
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))