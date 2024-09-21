#first create the empty list
print("FDS score:")
marks = []

print("Enter the number of students in the class :")
N= int(input())

print("Enter the marks of students :")

for i in range(N):
    element = int(input())
    marks.append(element)

print("Score obtained by the student is (-1 indicates the absent student) :")
print(marks)

#The average score of class

def average_score():
    sum=0
    cnt=0
    for i in range(len(marks)):
        sum = sum + marks[i]
        cnt=cnt+1

    print("Total score of the class is :",sum)
    print("Average score of the class is :",sum/cnt)

#Highest score and lowest score of class

def highest_lowest():
    temp=marks[0]
    for i in range(len(marks)):
        if temp < marks[i]:
            temp=marks[i]
    print("Highest mark is :",temp)

    for i in range(len(marks)):
        if marks[i] != -1:
            if temp > marks[i]:
               temp=marks[i]
    print("Lowest mark is :",temp)

#Count of students who were absent for the test

def absent_student():
    absent = []
    for i in range(len(marks)):
        if marks[i] == -1:
            absent.append(marks[i])
    print("Absent Students are :",len(absent))


def highest_frequency():
    list = []
    for i in range(0,len(marks)):
        cnt=0
        for j in range(i+1,len(marks)):
            if marks[i] == marks[j]:
                list.append(marks[i])
print("Number with highest frequency is :",list[0])


average_score()
highest_lowest()
absent_student()
highest_frequency()
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Output:
FDS score:
Enter the number of students in the class :
6
Enter the marks of students :
60
80
90
-1
99
95
Score obtained by the student is (-1 indicates the absent student) :
[60, 80, 90, -1, 99, 95]
Number with highest frequency is : list[0]
Total score of the class is : 423
Average score of the class is : 70.5
Highest mark is : 99
Lowest mark is : 60
Absent Students are : 1
Process finished with exit code 0
