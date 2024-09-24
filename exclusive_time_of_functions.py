# @leet start
class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        """
        This question asks us to figure out the amount of time a specific function
        took to run given a set of logs that describe how long each function ran
        for. It comes in the format of "{function_id}:{start | end}:{timestamp}".

        We have to return the amount of time each function exclusively ran on the cpu.
        To do so, we first parse the log by splitting it on colons, and then,
        we can simulate the run.

        If the action is start, we want to put our current function onto the stack,
        and then run the previous function until the current time, since it had
        exclusive time. We then update our running timestamp to the timestamp
        given by the function.

        Otherwise, the action is end, so we end the run of the function, by
        subtracting timestamp - current + 1 and then setting our current to
        timestamp + 1. We then record the amount of time in the answer array.
        """
        ans, stack, prev_time = [0] * n, [], 0

        for log in logs:
            fid, action, timestamp = log.split(":")
            fid, timestamp = int(fid), int(timestamp)

            if action == "start":
                if stack:
                    ans[stack[-1]] += timestamp - prev_time
                stack.append(fid)
                prev_time = timestamp
            else:
                ans[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        return ans


# @leet end


def test():
    assert 2 + 2 == 4
