def binary_search(arr, low, high, target):
    index_array = []

    while low<=high:
        mid=(low+high)/2
        if arr[mid]<target:
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            index_array = index_array + [mid]
            high=mid-1

    return index_array


arr = [10, 13, 18, 13, 18, 20, 18]
target = 18

arr.sort()
print(arr)
index = binary_search(arr, 0, len(arr) - 1, target)

if index == []:
    print("not present")
    print("%d not present in array" % target)
else:
    print("Index of {}: {}".format(target, index))

