from collections import defaultdict


# @leet start
class Node:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(Node)


class Trie:
    """
    This question asks us to implement a trie, a data structure for fast
    prefix searching.

    To do this, we first create a Node class, which has only two members, its
    children and whether or not it is the end of a word.

    The node's children will be a defaultdict of Node, so it will be char -> Node.

    When inserting a new word, we take the Trie's root (a dummy node), and then
    for every character, we set its child to a new node if we haven't seen that character before,
    otherwise, we simply move onto the next child node.

    If we search for a word, for every character in the word, we check if it exists
    in each node, and then check if our final pointer indicates it is a word.

    StartsWith is the same, we just dont have to check if the curr pointer is a word.
    """

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @leet end


def test():
    assert 2 + 2 == 4
