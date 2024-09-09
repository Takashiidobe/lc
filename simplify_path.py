# @leet start
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        This question gives us an absolute path for a unix style file system,
        which begins with a backslash and we need to transform it to a simplified
        path, where '.' means the current dir, '..' means the parent dir,
        consecutive slashes and treated as a single slash, and all other
        chars are file/dir names.

        We can solve this using a stack:

        We solve this by splitting the path by '/' and then if we see a portion
        with '..', we pop the top of the stack, if we see '.', or an empty
        portion, we do nothing, since this means keep on the same portion, and
        otherwise, append the portion to the stack.

        At the end, we prepend a backslash and join the stack with backslashes
        to get the final answer.
        """
        stack = []
        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()
            if portion == "." or not portion:
                continue
            else:
                stack.append(portion)
        return "/" + "/".join(stack)


# @leet end


def test():
    assert 2 + 2 == 4
