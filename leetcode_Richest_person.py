class Solution:
    def maximumWealth(self, accounts) -> int:
        wealth=0
        for i in accounts:
            wealth=max(sum(i),wealth)

        return wealth


ab=Solution()
lis=[[1,24,3],[3,2,1]]
print(ab.maximumWealth()
