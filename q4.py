#4.	Write a Python Program to Check Prime Number?
def checkprime(n):
    if(n==0 or n==1):
        print("invalid")
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return ("This is not prime")
        else:
            return ("This is Prime")
        

n=int(input("enter the number to be checked"))
print(checkprime(n))


