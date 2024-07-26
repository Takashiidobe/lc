class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_binary_tree(items):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


def to_bst(items):
    items.sort()

    def sorted_list_to_bst(items):
        if not items:
            return None
        mid = len(items) // 2
        root = TreeNode(items[mid])
        root.left = sorted_list_to_bst(items[:mid])
        root.right = sorted_list_to_bst(items[mid + 1 :])
        return root

    return sorted_list_to_bst(items)
