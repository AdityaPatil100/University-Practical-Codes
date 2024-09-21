def display(a,b):
    print("\n A = ",a)
    print("\n B = ",b)    
def Union(a,b,c):
    k = 0
    flag = 0
    c =  a.copy()
    k = len(c)
    for j in range(0, len(b)):
        flag = 0;
        for i in range(0,len(a)):
            if (a[i]==b[j]):
                flag = 1		
        if (flag == 0):
            c.insert(k,b[j])
            k = k + 1
    n = k
    return c
def Intersection(a,b,c):
    k = 0
    flag = 0
    for i in range(0, len(a)):
        flag = 1
        for j in range(0,len(b)):
            if (a[i] == b[j]):
                flag = 0
        if (flag == 0):
            c.insert(k,a[i])
            k = k+1
    n = k    
    return c
def difference(a,b,c):
    k = 0
    flag = 0
    for i in range(0, len(a)):
        flag = 1
        for j in range(0, len(b)):
            if(a[i]==b[j]):
                flag = 0
                break
        if (flag == 1):
            c.insert(k,a[i])
            k = k+1
    n = k;
    return c
def  NotBoth(a,b):
    c = []
    d = []
    result = []
    c = Union(a,b,c)
    d = Intersection(a,b,d)
    result = difference(c,d,result)
    print("\n Result = ",result)

def NeitherNor(U,a,b):
    c = []
    result = []
    c = Union(a,b,c)
    result = difference(U,c,result)
    print("\n Result = ",result)
def NotFootball(a,b,c):
    d =[]
    aAndb = Intersection(a,b,d)
    print("\n Students who play cricket and Football: ",aAndb)
    print("\n Students who play Badminton: ",c)
    #finding students who do not play Badminton but play both Cricket and Football
    result = []
    k = 0
    flag = 0
    for i in range(0, len(aAndb)):
        flag = 0
        for j in range(0, len(c)):
            if(aAndb[i]==c[j]):
                flag = 1
                break
            else:
                flag = 0
        if (flag == 0):
            result.insert(k,aAndb[i])
            k = k+1
    n = k;
    print("\n Result = ",result)	
    
    
#driver code
U = []
Cricket = []
Badminton = []
Football = []
Result = []
term =int(input("\n How many total students are there? "))
print(" Enter the names of students: ")
for i in range(0,term):
          name = input()
          U.append(name)
term1 = int(input("\n How many members play cricket ? "))
print("\n Enter the names of the players\n")
for i in range(0,term1):
    name = input()
    Cricket.append(name)
term2 = int(input("\n How many members play badminton ? "))
print("\n Enter the names of the players\n")
for i in range(0,term2):
    name = input()
    Badminton.append(name)

term3 = int(input("\n How many members play Football ? "))
print("\n Enter the names of the players\n")
for i in range(0,term3):
    name = input()
    Football.append(name)

while (True):
    print("Main Menu")
    print("\n1. List of Students who play both cricket and badminton")
    print("\n2. List of Students who play either cricket or badminton but not both")
    print("\n3. Number of Students who play neither cricket not badminton")
    print("\n4. Number of Students who play cricket and football but not badminton")
    print("\n5. Exit")
    print("Enter your choice: ")
    choice = int(input())
    if (choice == 1):
        display(Cricket, Badminton)
        print("\n Result = ",Intersection(Cricket, Badminton, Result)) #A intersection B
    elif (choice == 2):
        display(Cricket, Badminton)
        NotBoth(Cricket, Badminton)
    elif (choice == 3):
        display(Cricket, Badminton)
        NeitherNor(U,Cricket,Badminton)
    elif (choice ==4):
        NotFootball(Cricket,Football, Badminton)
    else:
        print("Exitting")
        break
#140 Lines code
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Output:
  PS C:\Users\HP> & C:/Users/HP/AppData/Local/Programs/Python/Python310/python.exe 

 How many total students are there: 5
 Enter the names of students: 
rohit
sachin 
virat
mahendra
reddy

 How many members play cricket ? 3

 Enter the names of the players

rohit
sachin
virat

 How many members play badminton ? 3

 Enter the names of the players

sachin
mahendra
reddy

 How many members play Football ? 3

 Enter the names of the players

rohit
virat
reddy
Main Menu

1. List of Students who play both cricket and badminton

2. List of Students who play either cricket or badminton but not both

3. Number of Students who play neither cricket not badminton

4. Number of Students who play cricket and football but not badminton

5. Exit
Enter your choice:
1

 A =  ['rohit', 'sachin', 'virat']

 B =  ['sachin', 'mahendra', 'reddy']

 Result =  ['sachin']
Main Menu

1. List of Students who play both cricket and badminton

2. List of Students who play either cricket or badminton but not both

3. Number of Students who play neither cricket not badminton

4. Number of Students who play cricket and football but not badminton

5. Exit
Enter your choice:
2

 A =  ['rohit', 'sachin', 'virat']

 B =  ['sachin', 'mahendra', 'reddy']

 Result =  ['rohit', 'virat', 'mahendra', 'reddy']
Main Menu

1. List of Students who play both cricket and badminton

2. List of Students who play either cricket or badminton but not both

3. Number of Students who play neither cricket not badminton

4. Number of Students who play cricket and football but not badminton

5. Exit
Enter your choice:
3

 A =  ['rohit', 'sachin', 'virat']

 B =  ['sachin', 'mahendra', 'reddy']

 Result =  []
Main Menu

1. List of Students who play both cricket and badminton

2. List of Students who play either cricket or badminton but not both

3. Number of Students who play neither cricket not badminton

4. Number of Students who play cricket and football but not badminton

5. Exit
Enter your choice:
4

 Students who play cricket and Football:  ['rohit', 'virat']

 Students who play Badminton:  ['sachin', 'mahendra', 'reddy']

 Result =  ['rohit', 'virat']
Main Menu

1. List of Students who play both cricket and badminton

2. List of Students who play either cricket or badminton but not both

3. Number of Students who play neither cricket not badminton

4. Number of Students who play cricket and football but not badminton

5. Exit
Enter your choice:
5
Exitting

