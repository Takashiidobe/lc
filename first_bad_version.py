# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return True


# @leet start
class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        This question asks us to find the first bad version introduced into
        a project, where the versions are from 1 to n and at some point, a
        change was introduced which broke the project. We can check if the project
        is a bad version with the function `isBadVersion`.

        We can do this by binary searching, to solve this in $O(log n)$ time.
        This is done by setting our left and right pointers to 1 and n, and
        then checking if the midpoint is a bad version. If it is, we set our
        right pointer to mid. Otherwise, we set our left pointer to mid + 1
        since we know that mid + 1 is the first possible bad version.
        We have to set r to m in the case since we don't know if m - 1 is a bad
        version.
        """
        l = 1
        r = n

        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l


# @leet end


def test():
    assert 2 + 2 == 4
