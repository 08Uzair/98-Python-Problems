# a=int(input("Entre a Number : "))
# if a <= 1:
#   print("The given Number is Not a Prime NUmber")

# for i in range(2, int(a**0.5) + 1):
#   if a% i == 0:
#     print("The given Number is not a Prime Number")
# print("The given Number is  A Prime number")
# print(i)
a=int(input("Entre a number : "))
for i in range (2,a-1):
  if a%i==0:
    print("It is not a prime Number")
  else:
    print("It is a prime number")
 