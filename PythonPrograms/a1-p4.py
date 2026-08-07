s=input("Enter String :")
ran=[s]
words=s.split()
print("Total Number :",len(words))

print("Total Number Of  Unique Words : ",len(set(words)))
print(" Longest Word         :",max(words,key=len))
print("Shortes Word          :",min(words,key=len))
dup=[]
for i in words:
    if(words.count(i)>1):
        if i not in dup:
            dup.append(i)
print(dup)
