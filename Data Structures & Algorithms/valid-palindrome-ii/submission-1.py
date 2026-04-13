class Solution:
    def validPalindrome(self, s: str) -> bool:
        str1 = ""
        str2 = ""

        skip_index = len(s) + 1
        right = len(s) - 1

        for i in range(len(s)):
            if s[i] != s[right]:
                str1 = s[0:i] + s[i + 1:]
                str2 = s[0:right] + s[right + 1:]
                break

            right -= 1

        return self.isPalindrome(str1) or self.isPalindrome(str2)
            


    def isPalindrome(self, s) -> bool:
        return s == s[::-1]