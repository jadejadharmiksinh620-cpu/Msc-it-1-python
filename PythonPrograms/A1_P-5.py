student_detail=[]
n=int(input("Enter The Number Of The STudents :"))
for i in range(n):
    name=input("\nEnter The Name :")
    roll=input("Enter The Roll Number:")
    mark=[]
    for j in range(5):
        mark.append(int(input("Enter The mark :")))
    total=sum(mark)
    percentage=total/5
    if(percentage>90):
        grade='A'
    elif(percentage>80):
        grade='B'
    elif(percentage>70):
        grade='C'
    elif(percentage>60):
        grade='D'
    elif(percentage>50):
        grade='E'
    else:
        grade="Fail"

    student_detail.append([name,roll,total,percentage,grade])
        
print(student_detail)
        
    
        
    
         
     
