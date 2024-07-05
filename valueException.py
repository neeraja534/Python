
def is_sorted(arr):
    for i in range(1,len(arr)):
        if(arr[i]>arr[i-1]):arr=[6,2,5,4,3]

print(arr)
arr.sort()
print("after sort")
print(arr)
is_sorted(arr)