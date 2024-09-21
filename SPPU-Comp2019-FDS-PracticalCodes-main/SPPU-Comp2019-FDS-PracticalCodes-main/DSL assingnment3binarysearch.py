def BinarySearch(arr,low,high,key):
    if high >= low:
        mid=(high+low)//2
        if (arr[mid]==key):
            return mid
        elif (arr [mid]> key):
            return BinarySearch(arr, low,mid-1, key)
        else:
            return BinarySearch(arr,mid+1,high,key)
    else:
      return -1
print("\nStudents attended training program:")
n=int(input())
arr=[]
for i in range(n):
    element=int(input())
    arr.append(element)
print("Enter Roll no. of students")
key=int(input())
result= BinarySearch(arr,0,len(arr)-1,key)
if result !=-1:
    print(key,"Found at index",str(result))
else:
    print(key,"Not found")

Output:
Students attended training program:
5
10
15
16
21
25
Enter Roll no. of students
16
16 Found at index 2
