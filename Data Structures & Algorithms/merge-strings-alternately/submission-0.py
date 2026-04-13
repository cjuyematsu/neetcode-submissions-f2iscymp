class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_len = len(word1)
        w2_len = len(word2)
        max_len = max(w1_len, w2_len)
        res = ""

        for i in range(max_len):
            c1 = word1[i] if i < w1_len else ""
            c2 = word2[i] if i < w2_len else ""
            res += c1 + c2

        return res
