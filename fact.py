def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def trail(n):
    fac=fact(n)   
    count=0
    i=5
    while(n//i!=0):
        count+= int(n/i)
        i=i*5
    return count
    
n=int(input("Enter the number to know its factorial and trail zeroes"))
result=fact(n)
print("Factorial of given number is :",result)
print("The Trail Zeroes of the given number is :",trail(n))