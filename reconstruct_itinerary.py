from collections import defaultdict


# @leet start
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        """
        This question asks us to find a path given a list of flights from one
        place to another.

        We also want to find the lexically shortest path if there is more
        than one path, so we first sort the tickets in reverse order before
        placing them in our adjacency list, because we want to pop them.
        We could sort in normal order and use a deque to pop from the beginning
        as well.

        Then, we define a DFS algorithm, which tries to fly through all of the
        flights by doing a post order traversal, where we want to visit each neighbor
        before we visit the current node.

        So, for each flight we see, we take its remaining flights, and take the last
        flight in its list of available flights, and DFS on that flight.
        When there are no flights left, we append our flight to the result.
        At the end, we're given a valid itinerary, just in reverse order.

        For example, with an itinerary of ((MUC, LHR), (JFK, MUC), (SFO, SJC),
        (LHR, SFO))

        We would fly like so:

        JFK ['MUC']
        MUC ['LHR']
        LHR ['SFO']
        SFO ['SJC']
        SJC []

        And then at SJC, we would have no flights to go to, so we would
        append ourselves to the output, and then go up the stack, to
        SFO, LHR, MUC, JFK.

        Which gives us:

        ['SJC', 'SFO', 'LHR', 'MUC', 'JFK']

        We can then just reverse this to get the correct answer.
        """
        tickets.sort(reverse=True)
        adj = defaultdict(list)

        for origin, dest in tickets:
            adj[origin].append(dest)

        def dfs(origin):
            flights_out = adj[origin]
            while flights_out:
                dfs(flights_out.pop())
            res.append(origin)

        res = []
        dfs("JFK")
        return res[::-1]


# @leet end


def test():
    assert 2 + 2 == 4
