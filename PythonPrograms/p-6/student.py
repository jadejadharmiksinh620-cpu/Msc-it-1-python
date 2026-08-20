def get_data():
    students=[]
    n=int(input("Enter How Many Students Data You Want to INserted :"))
    for i in range(n):
        name=input("Enter The Name : ")
        roll=int(input("Enter The Roll Number : "))
        m1=int(input("Enter The Mark of Python : "))
        m2=int(input("Enter The Mark of Linux : "))
        m3=int(input("Enter The MArk Of DSA : "))
        
        students.append({
            'name':name,
            'roll':roll,
            'python':m1,
            'linux':m2,
            'dsa':m3
        })
    return students
def cal_data(students):

    for i in students:
        
        m1=i['python']
        m2=i['linux']
        m3=i['dsa']
        total=m1+m2+m3
        per=total/3
        if per>90:
            grade='A'
        elif  per>80:
            grade='B'
        elif per>70:
            grade='C'
        elif per>60:
            grade='D'
        elif per>50:
            grade='E'
        else:
            grade='FAIL'
        i['total']=total
        i['percentage']=per
        i['grade']=grade
        
    return students
        
        
    