num=int(input("Enter a number:"))

div=0 #약수 개수 저장

def prime(n,div):
    if n==0: return div
    elif num%n==0:
        div+=1
        return prime(n-1,div)
    else: return prime(n-1,div)

if prime(num,div)==2: print(num,"is a prime number")
else: print(num,"is not a prime number")








