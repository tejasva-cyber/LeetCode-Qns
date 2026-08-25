class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []

        while queue:
            course = queue.pop(0)
            result.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return result if len(result) == numCourses else []