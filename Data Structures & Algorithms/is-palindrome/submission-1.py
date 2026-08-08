class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = [c.lower() for c in s if c.isalnum()]

        return cleaned_string == cleaned_string[::-1]