class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        lex_eq = []

        for i, letter in enumerate(order):
            d[letter] = i

        for word in words:
            cur = []

            for letter in word:
                cur.append(d[letter])
        
            lex_eq.append(cur)
        
        sorted_list = sorted(lex_eq)

        return lex_eq == sorted_list
                
