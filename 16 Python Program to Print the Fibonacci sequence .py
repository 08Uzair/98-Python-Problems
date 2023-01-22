# n=int(input("Entre a Number : "))
# def fib(n):
#     a=0
#     b=1
#     if n==1:
#      print(a)
#      print(b)
# for i in range(n):
#     c = a + b
#     print(c)
#     a = b
#     b = c

# fib(n)
def fibonacci(n):
    a=0
    b=1 
    if a==1:
        print(a)
        print(b)
    for  i in range(2,n):
        c = a + b
        print(c)
        a = b
        b = c

fibonacci(10)