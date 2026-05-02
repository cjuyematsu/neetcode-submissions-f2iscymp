class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        max_freq = 0
        j = 0
        max_len = 0

        for i in range(len(s)):
            window[s[i]] += 1

            if window[s[i]] > max_freq:
                max_freq = window[s[i]]

            if i - j + 1 - max_freq > k:
                window[s[j]] -= 1
                j += 1

            max_len = max(max_len, i - j + 1)
            
        return max_len
