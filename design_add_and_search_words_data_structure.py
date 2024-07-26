from collections import defaultdict


# @leet start
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False


class WordDictionary:
    """
    This problem asks us to design a trie that can handle matches with wildcards.
    This question is basically asking us to design the kleene star.

    So, as in a normal tree, addWord is the same - we have a root node, and
    for every character in the list, we keep adding it to the current pointer's
    children unless it already exists, then we do nothing (to not overwrite our
    progress) until we can't anymore then we set that character's is word to true.

    For the search function, we need to implement searching with wildcards.
    To do that, if we encounter a '.', we match any one character, so we increment
    our current index by one and then pass in all of the children of the current node
    to the search_wildcard function. If any of them match, we have a match.

    Otherwise the function works as usual. We pass in the current pointer to the function
    if needed.
    """

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]

        curr.is_word = True

    def search(self, word: str) -> bool:
        def search_wildcard(word, curr):
            for i, c in enumerate(word):
                if c == ".":
                    return any(
                        search_wildcard(word[i + 1 :], potential_match)
                        for potential_match in curr.children.values()
                    )
                if c not in curr.children:
                    return False
                curr = curr.children[c]
            return curr.is_word

        return search_wildcard(word, self.root)


def test():
    assert 2 + 2 == 4
