def calculation_grade_final_my(file_name):
   result = {}
   with open(file_name, 'r') as file:
      for line in file:
         data = line.strip().split(',')
         name = data[0].lower() 
         q_grades = list(map(int, data[1:7]))
         a_grades = list(map(int, data[7:11]))
         midterm_grade = int(data[11])
         final_grade = int(data[12])
            
        
         q_grades.sort()
         q_grades = q_grades[2:]   
        
         a_grades.sort()
         a_grades = a_grades[1:]
         
        
         q_average = sum(q_grades) / len(q_grades)
         a_average = sum(a_grades) / len(a_grades)
         
       
         total_grade = q_average * 0.25 + a_average * 0.25 + midterm_grade * 0.25 + final_grade * 0.25
         
         if total_grade >= 60:
            result[name] = "pass"
         else:
            result[name] = "fail"
   return result

file_name = "D:/New folder (2)/data.txt"    
x=calculation_grade_final_my(file_name)
print(x)