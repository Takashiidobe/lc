# @leet start
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        This question asks if we can make a circuit around an array if
        we're given an array of gas at a station and the cost to make it to the next
        station.

        To find out whether or not this is even feasible, the sum of the gas costs
        must be greater than the sum of the costs. If this is not the case, a
        complete circuit is not doable, and thus, we should return -1.

        If there is more gas than is required to be spent, we can complete the circuit.
        We then need to figure out the position to start.
        To do this, we can start out at the first index, and check when we have
        to spend more gas than we have available to us to make it to the next station.
        If that's the case, we continue on. If our current gas ever dips below 0,
        we know that we cannot make a circuit from the current index, so we
        assume that we can start at the index one past where we are, since
        that path could possibly be the starting index that solves the circuit.
        """
        total_gain, curr_gain, answer = 0, 0, 0

        for i, (gas_amount, gas_cost) in enumerate(zip(gas, cost)):
            gain = gas_amount - gas_cost
            total_gain += gain
            curr_gain += gain

            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1

        return answer if total_gain >= 0 else -1


# @leet end


def test():
    assert 2 + 2 == 4
