class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 1):
            return strs[0]

        cur = strs[0]

        for i in range(1, len(strs)):
            cur = self.commonPrefix(cur, strs[i])

        return cur


        
    def commonPrefix(self, str1, str2):
        cur = ""

        if(not str1 or not str2):
            return ""

        min_len = min(len(str1), len(str2))

        for i in range(min_len):
            if(str1[i] == str2[i]):
                cur += str1[i]
            else:
                return cur

        return cur
