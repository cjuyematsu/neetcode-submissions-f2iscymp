class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        boats = 0

        left, right = 0, n - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
            elif people[left] <= limit:
                boats += 1 
                        
            right -= 1

        return boats
