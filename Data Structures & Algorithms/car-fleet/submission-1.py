class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_pos = list(zip(position, speed))
        speed_pos.sort() 
        s = []
        fleets = 0

        for pos, speed in speed_pos:
            arrival_time = (target - pos) / speed
            if not s:
                s.append(arrival_time)
            elif arrival_time < s[-1]:
                s.append(arrival_time)
            else:
                while s and s[-1] <= arrival_time:
                    fleets -= 1
                    s.pop()

                s.append(arrival_time)
            
            fleets += 1

        return fleets
        