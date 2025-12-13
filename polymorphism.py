class India():
    def capital(self):
        print("New Dehli is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language in India") 

    def type(self):
        print("India is a developing country.")

#Class 2
class USA():
    def capital(self):
        print("Wasgington,D.C. is the capital of USA")
    
    def language(self):
        print("English is the primary language of USA")

    def type(self):
        print("India is a developed country.")

#Object Creation
obj_ind=India()
obj_usa=USA()

#Common Interface
for country in(obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()