Q. Write the python program for subtraction of matrix and for sparse matrix realization and operation on it-transpose
Answer: -
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
1. Python program for subtraction of matrix:
•	Source Code/Input: -
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
num1=[11,12,13],[14,15,16]
num2=[1,2,3],[1,3,2]
num3=[0,0,0],[0,0,0]
print("matrix A=")
for i in range(len(num1)):
    print(num1[i])
print("matrix B=")
for i in range(len(num1)):
    print(num2[i])
for i in range(len(num1)):
    for j in range(len(num1)+1):
        num3[i][j]=num1[i][j]-num2[i][j]   
print("Subtraction of matrix A and B")
for i in range(len(num3)):
    print(num3[i])
print("Code by: SEB06")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
•	Output:
matrix A=
[10, 15, 20]
[25, 30, 35]
matrix B=
[1, 2, 3]
[4, 5, 2]
Subtraction of matrix A and B
[9, 13, 17]
[21, 25, 33]
Code by: SEB06
_______________________________________________________________________________________________________________________________________________________________________________
2.sparse matrix realization and operation on it: Transpose
•	Source code/Input:
def create(s,row_num,col_num,non_zero_values):
    s[0][0]= row_num
    s[0][1] = col_num
    s[0][2] = non_zero_values        
    for k in range(1,non_zero_values+1):
        row = int(input("Enter row value: "))
        col = int(input("Enter col value: "))
        element = int(input("Enter the element: "))
        s[k][0]= row
        s[k][1] = col
        s[k][2] = element        
    
def display(s):
    print("Row\tcol\t Non_Zero_values")
    for i in range(0,(s[0][2]+1)): 
        for j in range(0,3): 
            print(s[i][j], "\t", end='') 
        print() 
def transpose(s1,row_num,col_num,s2,cols,non_zero_values):
    s2[0][0]= col_num
    s2[0][1] = row_num
    s2[0][2] = non_zero_values
    nxt=1
    for c in range(0,col_num+1):
    # for each column scan all the terms for a 'term' in that column 
        for Term in range(0,non_zero_values+1):
            if (s1[Term][0] == c):
	# Interchange Row and Column 
                s2[nxt][0] = s1[Term][1]
                s2[nxt][1] = s1[Term][0]
                s2[nxt][2] = s1[Term][2]
                nxt=nxt+1    
row_num = int(input("Input total number of rows for first matrix: "))
col_num = int(input("Input total number of columns for first matrix: "))
non_zero_values = int(input("Input total number of non-zero values: "))
cols =5
s = [[0 for col in range(cols)] for row in range(non_zero_values+1)]
trans_s = [[0 for col in range(cols)] for row in range(non_zero_values+1)]
create(s,row_num,col_num,non_zero_values)
print("Original sparse matrix is")
display(s)
transpose(s,row_num,col_num,trans_s,cols,non_zero_values)
print("Transposed sparse matrix is")
display(trans_s)
_______________________________________________________________________________________________________________________________________________________________________________
Output:
Input total number of rows for first matrix: 0
Input total number of columns for first matrix: 0
Input total number of non-zero values: 4
Enter row value: 1
Enter col value: 2
Enter the element: 13
Enter row value: 2
Enter col value: 3
Enter the element: 15
Enter row value: 5
Enter col value: 3
Enter the element: 16
Enter row value: 3
Enter col value: 6
Enter the element: 17
Original sparse matrix is
Row col  Non_Zero_values
0   0   4   
1   2   13   
2   3   15   
5   3   16   
3   6   17   
Transposed sparse matrix is
Row col  Non_Zero_values
0   0   4   
2   1   13   
3   2   15   
3   5   16   
6   3   17 
