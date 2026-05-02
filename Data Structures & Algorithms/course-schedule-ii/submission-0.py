from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        needed = [0] * numCourses
        prereq_to = defaultdict(list)
        taken = 0
        courses = []

        for course, prereq in prerequisites:
            needed[course] += 1
            prereq_to[prereq].append(course)
        
        q = deque(i for i in range(numCourses) if needed[i] == 0)

        while q:
            course = q.popleft()
            courses.append(course)
            taken += 1

            for neighbor in prereq_to[course]:
                needed[neighbor] -= 1

                if needed[neighbor] == 0:
                    q.append(neighbor)
            
        return courses if taken == numCourses else []