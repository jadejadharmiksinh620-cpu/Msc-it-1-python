n=int(input("Enter The Size of List :"))
b=[]
for i in range (n):
    a=int(input())
    b.append(a)

print("Consecutive Number :")
for i in range (n-1):
    if b[i] ==b[i+1]:
        print(b[i])
