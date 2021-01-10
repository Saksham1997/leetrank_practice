class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        out=[]
        for i,j in zip(index,nums):
            out.insert(i,j)

        return out
        
