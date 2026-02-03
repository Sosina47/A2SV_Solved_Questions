if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score]) 
    
    students.sort(key = lambda x: (x[1], x[0]))
    
    second = students[0]
    for student in  students:
        if second[1] != student[1]:
            second = student
            break
            
    for student in students:
        if student[1] == second[1]:
            print(student[0])
