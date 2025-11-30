#Create class
class Employee:

    #Intialising
    def __init(self):
        print("Employee created")

        #calling destructor
        def __del__(self):
            print("Destructor called")

def Create_obj():
    print('Making Obejct...')
    obj=Employee()
    print('function end...')
    return obj

print('Calling Create_obj()function...')
obj = Create_obj()
print('Program End...')