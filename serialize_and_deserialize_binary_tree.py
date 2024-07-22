from utils import TreeNode
from collections import defaultdict, deque
from itertools import chain


# @leet start
class Codec:
    """
    This class serializes and deserializes a binary tree.
    """

    def serialize(self, root):
        """
        The serialize function takes a treenode and returns a string.
        It does a bfs (for a level-order traversal) of the nodes and then
        puts them in a defaultdict.
        Finally, since nulls are allowed, the last level will be all nulls.
        That is removed from the dict with serialized.popitem()
        and then joined with '#' to send over the wire.
        """
        if not root:
            return ""
        serialized = defaultdict(list)
        q = deque()
        q.append((root, 0))

        while q:
            node, level = q.popleft()
            if not node:
                serialized[level].append(None)
                continue
            else:
                serialized[level].append(node.val)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))

        serialized.popitem()
        return "#".join(map(lambda x: str(x), list(chain(*serialized.values()))))

    def deserialize(self, data):
        """
        This function takes the string representation, splits it for every #
        and then returns the root node that represents that tree.

        It takes the first node of that list and creates a root, and then
        for each node in the queue, it takes the next left and right nodes
        and moves through the queue, adding nodes back onto the queue, for each
        remaining item in the string.
        """
        if not data:
            return None
        l = data.split("#")
        root = TreeNode(int(l[0]))
        q = deque()
        q.append(root)
        i = 1
        while q and i < len(l):
            node = q.popleft()
            if l[i] != str(None):
                left = TreeNode(int(l[i]))
                node.left = left
                q.append(left)
            i += 1
            if l[i] != str(None):
                right = TreeNode(int(l[i]))
                node.right = right
                q.append(right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @leet end


def test():
    assert 2 + 2 == 4
