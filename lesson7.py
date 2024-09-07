grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_dict=(sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),
         sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4]))
print(my_dict)
my_dict3=sorted(students)
my_dict2=dict(zip(my_dict3,my_dict))
print(my_dict2)