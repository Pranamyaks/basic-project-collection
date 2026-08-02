def student_grade_calculator(filename):
    with open(filename,'r') as file:
       count=0
       for line in file:
           #print(line.strip())
           #print(line.split())
           data=line.split()
           name=data[0]
           marks=data[1:]
           #print(data[0])
           #print(marks)
           new_marks=[]
           for m in marks:
               new_marks.append(int(m))
               #print(new_marks)       
           avg=sum(new_marks)/len(new_marks)
           #print(avg)
           if avg>=90:
              grade="A"
           elif avg>=75:
              grade="B"
           elif avg>=45:
              grade="C"
           elif(avg>=25):
              grade="D"
           else:
              grade="Fail!!"
           print(f"{name}|Avg:{avg}|Grade:{grade}")
           count+=1
       file.close()    
       print("Total students:",count)
student_grade_calculator('info.txt')       
