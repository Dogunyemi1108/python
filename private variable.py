#Class creation
class myClass:
    #private variable
    _privateVar= 27

    #private method
    def __privMeth(self):
        print("I'm inside class myclass")
    
    def hello(self):
        print("Private variable value:",myClass.__privateVar)
foo = myClass()
foo.hello()
foo.__privMeth