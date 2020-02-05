def power(num,n):
    if(n==0):
        return(1)
    if(n==1):
        return (num)
    if(n!=1):
        return(num*power(num,n-1))
num=int(input("Enter base: "))
n=int(input("Enter exponential value: "))

print("Result:",power(num,n))
    


