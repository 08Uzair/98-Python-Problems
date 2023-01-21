a=int(input("Enter a Number : "))
b=list(map(int,str(a)))
print(b)
n=(len(b))
sum = 0
for i in range(0,n):
    sum = sum + b[i]**n
if sum==a:
    print("The given number is an Armstrong Number")
else:
    print("The given number is not an armstrong number")