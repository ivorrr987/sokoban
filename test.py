arr1 = [1,2,3,4,5]
print(arr1)
def add_arr(arr):
    arr.append(arr[len(arr)-1]+1)
    
for i in range(5):
    add_arr(arr1)
print(arr1)