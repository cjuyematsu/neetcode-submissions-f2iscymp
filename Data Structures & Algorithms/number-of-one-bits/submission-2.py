class Solution:
    def hammingWeight(self, n: int) -> int:    
        mask = 1 << 31
        count = 0

        for i in range(32):
            if n & mask:
                count += 1
            
            mask >>= 1

        return count