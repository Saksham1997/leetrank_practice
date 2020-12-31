def removeDuplicates(nums):
    nums[:] = list(set(nums))
    nums.sort()
    return len(nums)

nums = [1,1,2]
length = removeDuplicates(nums)
print(nums)
