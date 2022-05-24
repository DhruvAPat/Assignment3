year=int(input("enter the year"))
if((year%4==0) & (year%100!=0)):
    print("The Year {} is a leap year".format(year))
elif(year%400==0):
    print("The Year {} is a leap Year".format(year))
else:
    print("The Year {} is not a leap Year".format(year))
