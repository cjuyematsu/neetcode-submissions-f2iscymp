class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s.lower() if char.isalnum())
        return cleaned == cleaned[::-1]