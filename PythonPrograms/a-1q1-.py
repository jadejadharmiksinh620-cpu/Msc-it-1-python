n=int(input("Enter Size of Array :"))
rno=[]

for i in range (n):
    rno.append(int(input()))
print(rno)
m=max(rno)
n=min(rno)
for j in range (1,m+1):
    if j not in rno:
        print(j)