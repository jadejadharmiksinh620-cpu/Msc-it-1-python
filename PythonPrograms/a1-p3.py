pas=input("Enter The Password :")
lst=[]

upper=0
lower=0
digit=0
special=0
repeat=0
psw=0

for i in pas:
    if i >='A' and i<='Z':
        upper=upper+1
    elif i>='a' and i<='z':
        lower=lower+1
    elif i>='0' and i<='9':
        digit=digit+1
    else:
        special=special+1
for i in range (len(pas)-1):
    if pas[i] == pas[i+1]:
        repeat=repeat+1



if upper ==0:
    print("Uppercase is missing in the Password !")
else:
    psw =psw+1
    
if lower ==0:
    print("Lowercase is missing in the Password !")
else:
    psw=psw+1
if digit ==0:
        print("Digit  is missing in the Password !")
else:
    psw=(psw+1)
if repeat !=0:
    print(" Character are repeat in your password !")
else:
    psw=psw+1
if special ==0:
    print("! Special Character are Missing ")
else:
    psw=psw+1
if psw==5:
        print("Password is Strong")


