class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        final_word=''
        final_word2=''
        for i in range(len(word1)):
            final_word=final_word+word1[i]
        for i in range(len(word2)):
            final_word2=final_word2+word2[i]
        if final_word==final_word2:
            return True
        else:
            return False

ab=Solution()
print(ab.arrayStringsAreEqual(["ab", "c"],["a", "bc"]))
