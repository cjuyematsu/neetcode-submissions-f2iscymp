class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            equal = False
            if a < 0 and s:
                while s:
                    right = s.pop()
                    if right < 0:
                        s.append(right)
                        s.append(a)
                        break
                    else:
                        if right == abs(a):
                            equal = True
                            break
                        elif right > abs(a):
                            s.append(right)
                            break
                    
                if not s and not equal:
                    s.append(a)

            else:
                s.append(a)
            

        return s
                        