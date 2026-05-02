class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            stack.append(intervals[i])
            
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

            i += 1
        
        stack.append(newInterval)

        while i < n:
            stack.append(intervals[i])
            i += 1
        
        return stack