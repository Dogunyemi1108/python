#create class
class Parrot:

    #class attribute
    species="bird"

    #instance attribute
    def __init__(self,name, age):
        self.name=name
        self.age=age

#instantiate the Parrot class
blu=Parrot("Blu",10)
woo=Parrot("Woo",15)

#access the instance attributes
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))



