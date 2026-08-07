from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        res = []

        for s in strs:
            sorted_s = sorted(s)

            anagrams["".join(sorted_s)].append(s)

        
        for vals in anagrams.values():
            res.append(vals)

        
        return res
