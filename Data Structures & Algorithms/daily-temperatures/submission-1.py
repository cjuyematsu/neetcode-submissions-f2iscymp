class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not s:
                s.append((i, temp))
            elif temp <= s[-1][1]:
                s.append((i, temp))
            else:
                while s:
                    index, t = s.pop()
                    if t < temp:
                        res[index] = i - index
                    else:
                        s.append((index, t))
                        s.append((i, temp))
                        break
                                
                if not s:
                    s.append((i, temp))            
        
        return res
