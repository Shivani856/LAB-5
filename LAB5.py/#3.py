#a)
n=int(input("enter a digit "))
i=0
while i<n:
    i+=1
    print("."*i)

#b)
n=int(input("enter a digit "))
i=0

while i<n:
    i+=1
    j=n-i
    print(" "*j + "."*i)


#C)
n=int(input("enter a digit "))
i=0

while i<n:
    i+=1
    j=n-i
    k=i-1

    print(" "*j + "."*i+"."*k)
    
