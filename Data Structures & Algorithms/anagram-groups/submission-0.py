from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sorted_string = "".join(sorted(s))
            anagrams[sorted_string].append(s)
        
        return [group for group in anagrams.values()]