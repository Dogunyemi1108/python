#create a class
class pair_elements:
    def twoSum(self,nums,target):
        #create an empty dictionary
        lookup= ()

        #Iterate through the tuple
        for i, num in enumerate(nums):
               if target - num in lookup:
                  return(lookup[target-num]),

               lookup[num]=i
            
#take in put of dum from the user
value = int(input("Enter sum for which you want to take make this search:"))
print("index1=%d, inde")