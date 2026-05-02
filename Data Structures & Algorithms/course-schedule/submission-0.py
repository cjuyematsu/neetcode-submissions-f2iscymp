from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        needed_prereqs = [0] * numCourses
        prereq_to = defaultdict(list)
        taken = 0

        for course, prereq in prerequisites:
            needed_prereqs[course] += 1
            prereq_to[prereq].append(course)
        
        q = deque([i for i in range(numCourses) if needed_prereqs[i] == 0])

        while q:
            course = q.pop()
            taken += 1

            for course in prereq_to[course]:
                needed_prereqs[course] -= 1

                if needed_prereqs[course] == 0:
                    q.append(course)
                
        return taken == numCourses