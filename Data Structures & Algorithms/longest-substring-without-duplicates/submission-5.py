class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        seen = set()
        j = 0
        longest_substring = 1

        for i in range(len(s)):
            if s[i] in seen:
                longest_substring = max(longest_substring, i - j)
                while j < i:
                    if s[j] == s[i]:
                        j += 1
                        break
                    else:
                        seen.remove(s[j])
                        j += 1

            elif i == len(s) - 1:
                longest_substring = max(longest_substring, i - j + 1)

            seen.add(s[i])

        return longest_substring
