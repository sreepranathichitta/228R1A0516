x=int(input("enter a year"))
if(x%4==0)and(x%100!=0):
    print(x," is leap year")
else:
    print(x," is not a leap year ")