from itertools import chain
from collections import deque
from typing import Optional
from utils import TreeNode


# @leet start
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        """
        This problem asks us to show the right side view of a binary tree.
        If we were on the right side of the binary tree, which nodes would we see?
        Imagine a level-order traversal of the tree. We'd always want the rightmost
        node. So, we do a traversal level by level, and left to right, and then place
        the last node we've seen on each level into a list and return the list.

        This works because we always save the last node which we've seen, and since
        we're going from left to right, that will always be the rightmost node.
        """
        if not root:
            return []

        res = []
        q = deque()
        q.append((root, 0))

        while q:
            node, level = q.popleft()
            if len(res) <= level:
                res.append([node.val])
            else:
                res[level][-1] = node.val

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return list(chain(*res))


# @leet end


def test():
    assert 2 + 2 == 4
