class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cur_change = defaultdict(int)

        for bill in bills:
            if bill == 5:
                cur_change[5] += 1
            
            if bill == 10:
                if cur_change[5] == 0:
                    return False
                
                cur_change[5] -= 1
                cur_change[10] += 1
            
            if bill == 20:
                if cur_change[10] >= 1 and cur_change[5] >= 1:
                    cur_change[10] -= 1
                    cur_change[5] -= 1
                
                elif cur_change[5] >= 3:
                    cur_change[5] -= 3

                else:
                    return False
        
        return True
