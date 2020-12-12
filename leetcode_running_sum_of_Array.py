class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cum_lis=[]
        sum_cum=0
        for i in range(len(nums)):
            sum_cum+=nums[i]
            cum_lis.append(sum_cum)

        return cum_lis
