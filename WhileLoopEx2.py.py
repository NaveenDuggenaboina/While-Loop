#write a python prgm which will generating  n to 1 where n is +ve interger value
# 10 9 8 7 6 5 4 3 2 1
#WhileLoopEx2.py
n=int(input("enter how many numbers u want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("="*100)
    print("numbers within {} to 1".format(n))
    print("=" * 100)
    i=n
    while(i>=1):
        print("\t\t\t{}".format(i))
        i=i-1
    else:
        print("=" * 100)

