class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)-1
        for i in range(0,(length+1)//2):
            temp = s[length-i]
            s[length-i] = s[i]
            s[i] = temp
