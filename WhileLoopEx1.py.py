#write a python prgm for generating 1 to 10 numbers
#1 2 3 4 5 6 7 8 9 10
#WhileLoopEx1.py
n=int(input("enetr how many numbers u want to generate:"))
i=1 #Initilization Part
while(i<=n): # Cond Part
    print("{}".format(i))
    i=i+1 # Updation Part
else:
    print("i am from else part of while loop")
print("other stmts")