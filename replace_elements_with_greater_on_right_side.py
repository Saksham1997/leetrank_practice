def replaceElements(arr):
    for i in range(len(arr)-1) :
            maxi = max(arr[i+1:])
            arr[i] = maxi
    arr[-1] = -1
    return arr


arr = [17,18,5,4,6,1]
arr = replaceElements(arr)

print(arr)
