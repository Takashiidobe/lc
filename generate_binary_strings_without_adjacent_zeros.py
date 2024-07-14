# @leet start
class Solution:
    def validStrings(self, n: int) -> list[str]:
        """
        This code manually generates all the binary strings for numbers from 0..2^n
        And then makes sure there's at least one 1 every two digits.

        To generate the strings properly, since they have to be padded properly,
        the format function is used with the string f"#0{n + 2}b".
        This guarantees that the generated string is left padded with enough zeroes.
        Finally, the validate function checks to make sure there's at least one 1 every two digits.
        """
        strs = [format(i, f"#0{n + 2}b")[2:] for i in range(2**n)]

        def validate(s):
            prev_one = True
            for c in s:
                if not prev_one and c == "0":
                    return False
                prev_one = c == "1"
            return True

        return [s for s in strs if validate(s) if len(s) == n]


# @leet end
def test():
    pass
