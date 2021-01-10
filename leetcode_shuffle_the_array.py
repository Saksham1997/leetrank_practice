class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lis =[]
        i=0
        for i in range(int(len(nums)/2 + 1)-1):
            lis.append(nums[i])
            try:
                lis.append(nums[n+i])
            except:
                print(n,i)

        return lis
