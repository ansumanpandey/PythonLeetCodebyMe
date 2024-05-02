class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge=""
        for i in range(max(len(word1),len(word2))):
            if i<len(word1) and i<len(word2):
                merge= merge+word1[i]+word2[i]
            elif i<len(word1) and i>=len(word2):
                merge= merge+word1[i]
            else:
                merge= merge+word2[i]

        return merge



