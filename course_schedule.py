from collections import defaultdict, deque


# @leet start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        This question asks us to find if we can finish all the courses provided,
        where each course may have any number of prerequisites.

        To do this, we can do a topological sort, where we first start off by
        taking all the courses with no prerequisites. While we're doing that,
        we find all courses that the current course is a prerequisite to, and
        remove it from that course. If we've taken a course that is the last
        prerequisite for a given course, we can add that course to our queue
        and take that course as well.

        If we can follow this pattern and take all the classes, then the schedule
        is completeable. If not, then it isn't completeable, either because
        you can't take a given prerequisite (A requires B, but B is not a course
        that can be completed) or there's a cycle (A requires B and B requires A),
        which isn't completable.
        """
        indegrees = defaultdict(set)
        outdegrees = defaultdict(set)

        for course, prereq in prerequisites:
            indegrees[prereq].add(course)
            outdegrees[course].add(prereq)

        q = deque([course for course in range(numCourses) if not indegrees[course]])

        courses_taken = 0
        while q:
            course = q.popleft()
            courses_taken += 1

            for outdegree in outdegrees[course]:
                indegrees[outdegree].remove(course)
                if not indegrees[outdegree]:
                    q.append(outdegree)

        return courses_taken == numCourses


# @leet end


def test():
    assert 2 + 2 == 4
