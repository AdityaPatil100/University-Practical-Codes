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
print("\nEnter the number of element:")
n=int(input())
arr=[]
for i in range(n):
    element=int(input())
    arr.append(element)
print("Enter key")
key=int(input())
result= BinarySearch(arr,0,len(arr)-1,key)
if result !=-1:
    print(key,"Found at index",str(result))
else:
    print(key,"Not found")
  
  
 #---------------------------------------------------------------------------------------------
Output:
  Enter the number of element:
5
10
20
30
40
50
Enter key
30
30 Found at index 2

Process finished with exit code 0
