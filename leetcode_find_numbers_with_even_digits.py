class Solution:
    def findNumbers(nums):
        c=0
        for i in range(len(nums)):
            if (nums[i]>=10 and nums[i]<=99)or(nums[i]>=1000 and nums[i]<=9999)or(nums[i]>=100000 and nums[i]<=999999):
                print(nums[i])
                c+=1;

        return c;
ab=Solution()
lis=[12,235,1234,9999,2311]
print(ab.findNumbers(lis)
