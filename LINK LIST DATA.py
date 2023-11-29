gread_table = {'A':4.0,'B':3.3,'C':2.6,'D':1.5,'F':0}

num_course = int(input('enter the num of courses in semister'))

total_gread_points=0

total_credit=0

for i in range(num_course):
    
     gread=(input(f'enter the gread of the subject:{i+1}...'))    
     
     credit=int(input(f'enter the credit of this subject:{i+1}...'))
     
     gread_points = gread_table[gread] * credit
     
     total_gread_points = total_gread_points + gread_points
     
     total_credit = total_credit + credit
     
gpa = total_gread_points / total_credit

print(gpa)