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
student_detail.sort(key=lambda x: x[2],reverse=True)
current_rank=1
for i  in range(len(student_detail)):
    if i>0 and student_detail[i][2]<student_detail[i-1][2]:
        current_rank=i+1

    student_detail[i].append(current_rank)


print(f"{'rank':<6}{'name':<15}{'roll':<8}{'Total':<8}{'Percentage':<12}{'Grade':<6}")


for s in student_detail:
    print(f"{s[5]:<6}{s[0]:15}{s[1]:<10}{s[2]:<8}{s[3]:<12.2f}{s[4]:<6}")
        
    
        
    
         
     
