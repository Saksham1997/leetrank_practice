def checkIfExist(arr) -> bool:
    nums = [i*2 for i in arr]
    if nums.count(0) > 1:
        return True
    for i in nums :
        if i in arr and i!=0 :
            print (i)
            return True

    return False


nums = [-2 , 0 , 4, 6, 8, -9]
print(checkIfExist(nums))
