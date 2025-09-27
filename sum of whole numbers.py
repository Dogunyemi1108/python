#input an interger value
n = int(input("Enter the number whose sum you want to find:"))
sum = 0

#Iterates for n+1 times: i=i to n+1
for i in range(1, n+1):
    sum=sum+i
    print("\nSum, =", sum)