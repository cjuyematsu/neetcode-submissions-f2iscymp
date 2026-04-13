class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        rev_people = people[::-1]
        n = len(people)
        boats = 0

        left, right = 0, n - 1

        while left <= right:
            if rev_people[left] + rev_people[right] <= limit:
                boats += 1
                right -= 1
            elif rev_people[left] <= limit:
                boats += 1 
                        
            left += 1

        return boats
