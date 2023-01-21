a=int(input("Enter Number of Year : "))
if (a%400==0) and (a%100==0):
    print("The Given Year is a Leap Year")
elif (a%4==0 ) and (a%100!=0):
    print("The Given Year is a Leap Year")
else:
    print(f"{a} is not a leap Year")