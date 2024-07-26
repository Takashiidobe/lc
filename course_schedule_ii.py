from collections import defaultdict, deque


# @leet start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        This function finds an ordering of a graph given that some nodes have
        dependencies.

        We first iterate through the prerequisites by adding each course's
        prerequisites to a dictionary that lists its indegrees (each course requires
        these prerequisites) and its outdegrees (where each prereq lists which
        courses it is required for)

        Then we populate a queue with the nodes without indegrees (no prerequisites)

        And then, for each node in the queue, we complete its courses, by looking
        at each of its outdegrees, and then checking to see if that course has
        no more dependencies by checking that course's indegrees.

        If that's the case, we add the course we're checking to the queue and
        continue on.

        We have a valid ordering if we can visit all nodes. If we cannot, there is
        a cycle and no topological ordering.
        """
        indegrees = defaultdict(set)
        outdegrees = defaultdict(set)
        for course, prereq in prerequisites:
            indegrees[course].add(prereq)
            outdegrees[prereq].add(course)

        q = deque([c for c in range(numCourses) if c not in indegrees])

        schedule = []

        while q:
            course = q.popleft()
            schedule.append(course)

            for outdegree in outdegrees[course]:
                indegrees[outdegree].remove(course)
                if not indegrees[outdegree]:
                    q.append(outdegree)

        return schedule if len(schedule) == numCourses else []


# @leet end


def test():
    assert 2 + 2 == 4
