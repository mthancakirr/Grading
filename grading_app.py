def calculate_grade(line):
    line=line[:-1]
    list=line.split(":")
    name_of_student=list[0]
    grades=list[1].split(",")
    ggrade1=int(grades[0])
    ggrade2=int(grades[1])
    ggrade3=int(grades[2])
    average=int((ggrade1+ggrade2+ggrade3)/3)
    if 90<=average and average <=100:
        letter_grade="AA"
    elif 85<= average <=89:
        letter_grade="BA"
    elif 80<= average and average <=84:
        letter_grade="BB"
    elif 75<= average and average  <=79:
        letter_grade="CB"
    elif 74<= average and average  <=70:
        letter_grade="CC"
    elif 65<= average and average  <=69:
        letter_grade="DC"
    elif 60<= average and average  <=64:
        letter_grade="DD"
    elif 50<= average and average  <=59:
        letter_grade="FD"
    elif average<50:
        letter_grade="FF"
    else:
        letter_grade="FF"
    return name_of_student+":" +letter_grade+"\n"
def read_grades():
    with open("exam_grades.txt","r",encoding="utf-8") as file:
       for line in file:
           print(calculate_grade(line)) 
def write_grades():
    name=input("Name of student:")
    surname=input("Surname of student:")
    grade1=input("Grade1:")
    grade2=input("Grade2:")
    grade3=input("Grade3:")
    with open("exam_grades.txt","a",encoding="utf-8") as file:
        file.write(name+ " "+ surname+ ":"+grade1+","+grade2+","+grade3+"\n")

def save_grades():
    with open("exam_grades.txt","r",encoding="utf-8") as file:
        list=[]
        for i in file:
            list.append(calculate_grade(i))
        with open("exam_results.txt","w",encoding="utf-8") as file2:
            for i in list:
                file2.write(i)
while True:
    operation=input("1-Read Gradees\n2- Write Grades\n3-Save Grades\n4-Exit\n")
    if operation=="1":
        read_grades()
    if operation=="2":
        write_grades()
    if operation=="3":
        save_grades()
    if operation=="4":
        break
    else:
        print("Please enter a valid number(1,2,3,4).")