def dele(nums,val):
    if not nums :
        return 0
    nums[:] = [i for i in nums if i!=val]
    return len(nums)

nums = [2,2,3]
len = dele(nums,2)
print(nums)
