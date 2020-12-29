class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = 0
        j = m
        while j<m+n :
            nums1[j] = nums2[k]
            j+=1
            k+=1
        #print(nums1)
        nums1.sort()
