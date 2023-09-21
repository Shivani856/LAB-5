
a=int(input("enter a  number "))
b=int(input("enter a  number "))
L=min(a,b)
while  True :
    if L%a==0 and L%b==0:
        print(L)
        break
    else:
        L+=1


