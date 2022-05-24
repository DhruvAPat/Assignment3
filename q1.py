#1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?

N=float(input("Enter the no to check"))
if N==0:
    print("The given input is zero")
elif N>0:
    print("The number {} is a positive integer".format(N))
else:
    print("The number {} is a negative integr".format(N))