def report(students):
    print(" Rank Name     Roll  Python   Linux  DSA Total Per Grade ")
    for i in students:
        print(i['rank'],i['name']   ,i['roll'],i['python'],i['linux'],i['dsa'],i['total'],i['percentage'],i['grade'])
