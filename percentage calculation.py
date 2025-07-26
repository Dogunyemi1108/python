print("Enter Marks Obtained in 4 subjects")
maths =int(input("maths:"))
english =int(input("english:"))
science =int(input("science:"))
french =int(input("french:"))

sum=maths+english+science+french
print("sum of math,english,science and french")
 
perc = (sum/400)*100

print(end="percentage mark=")
print(perc)