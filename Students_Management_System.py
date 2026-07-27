report = {}
while True:
    a = int(input("Enter\n 1 for Adding a new student \n 2 for Updating any student \n 3 for Deleting a student \n 4 for Comparing all students \n 5 for exit the program \n : "))
    #ADD A STUDENT
    if a == 1:
        key = input("Enter Student's Name: ")
        value = int(input(f"Enter Marks of {key} : "))
        report[key] = value
    #UPDATE ANY STUDENT 
    elif a == 2:
       n = input("Enter the name of that student: ")
       if n in report:
            b = int(input("Enter \n 1 for Student \n 2 for marks \n : "))
            if b == 1:
                x = input("Enter the new name: ")
                report[x] = report.pop(n)
            if b == 2:
                y = int(input("Enter new marks: "))
                report[n] = y
            else:
                print(f"Student {n} was not in records")
    #DELETE ANY STUDENTel
    elif a == 3:
        z = input("Enter the student name, you want to remove: ")
        if z in report:
            del report[z]
        else:
            print(f"{z} is not present in the data")
    #COMPARE MARKS
    elif a == 4:
        p = sorted(report.items(), key=lambda item: item[1], reverse=True)
        for key, value in p:
            print(f"{key}: {value}")
    elif a == 5:
        break
    else:
        print(f"{a} is not currently active in our services.\n SORRY!")
