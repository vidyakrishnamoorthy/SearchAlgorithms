def linear_search(arr, target):
    index_array = []

    for i in range(0, len(arr)):
        if arr[i] == target:
            index_array = index_array + [i]

    return index_array


arr = [10, 13, 18, 13, 18, 20, 18]
target = 18

print(arr)
index = linear_search(arr, target)

if index == []:
    print("not present")
    print("%d not present in array" % target)
else:
    print("Index of {}: {}".format(target, index))

