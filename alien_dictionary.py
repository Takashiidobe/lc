from collections import Counter, defaultdict, deque


# @leet start
class Solution:
    def alienOrder(self, words: list[str]) -> str:
        """
        This question asks us to return an ordering of characters given a set
        of sorted words.

        First, we describe the relation between the characters. We do this by
        extracting the first character of each pair that doesn't match, and
        noting that the left side char comes before the right side.

        For these words:

        wrt
        wrf
        er
        ett
        rftt

        the pairs would be (wrt, wrf), (wrf, er), (er, ett), (ett, rftt).

        For each pair, we want to find which ones come before, so:

        (wrt, wrf) = t -> f (since wr are the same, t and f are the first differing
        characters, and t is on the left side of our pair, so t comes before f).
        (wrf, er) = w -> e (since w and e don't match, and w is on the left).
        (er, ett) = r -> t (since e matches for both, and r is on the left).
        (ett, rftt) = e -> r (since e must come before r).

        As well, we want to create an indegree map that counts how man indegrees
        each node has. For this graph:

        t -> f
        w -> e
        r -> t
        e -> r

        The indegrees are:

        r -> 1
        t -> 1
        f -> 1
        e -> 1
        w -> 0

        In this case, we find any node with indegree 0 and do a topological sort.
        So in the above case, we visit w, add it to our output, and then check
        if its children, in this case, e are visitable.

        e has an indegree of 1, so after w is visited, it is visitable, so
        we visit e.

        Then, e allows us to visit r, which also has an indegree of 1, so after
        visiting e, r is visitable.

        Then we visit r, which has a child of t, and we can visit t after visiting
        r because it has an indegree of 1.

        Then we visit t, which allows us to visit f.

        This allows us to construct the string "wertf", which is the only valid
        ordering for this example, but other examples may have more orderings.

        We make sure that we've counted every char in the original set of words
        before returning the joined string.

        """
        adj_list = defaultdict(set)
        indegrees = Counter({c: 0 for word in words for c in word})

        for l, r in zip(words, words[1:]):
            for c, d in zip(l, r):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        indegrees[d] += 1
                    break
            else:
                if len(r) < len(l):
                    return ""

        output = []
        q = deque([c for c in indegrees if indegrees[c] == 0])
        while q:
            c = q.popleft()
            output.append(c)
            for d in adj_list[c]:
                indegrees[d] -= 1
                if indegrees[d] == 0:
                    q.append(d)

        if len(output) < len(indegrees):
            return ""
        return "".join(output)


# @leet end


def test():
    assert 2 + 2 == 4
