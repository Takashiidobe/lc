# @leet start
class Codec:
    def encode(self, strs: list[str]) -> str:
        """
        This function encodes a list of strings into a singular string.
        This does this with varchar encoding. Since the string can have any ASCII
        character in it, it does this by first encoding the length of the string,
        then a delimiter of some kind (`#` in this case), and then the string.
        This allows the decoder to first parse digits and recreate the length,
        Then when it sees the hashtag, it knows to stop parsing digits.
        Finally, it parses `n` characters, which stops it before the length of the next str.

        Since this problem says that only ASCII characters are allowed, the most efficient
        way to encode the string would be to use a non-ASCII character as a delimiter, since
        that only requires one character per string to encode, whereas requires the length
        of the string in decimal form + a hashtag character.

        However, that approach doesn't work for any arbitrary character, since that
        could show up in the middle of a str and the tokenizer would cut a string into two
        that it shouldn't have. Likewise, simply encoding the length doesn't work, because numbers
        can appear at any time in the string.
        """
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        """
        This function decodes the encoded string. The way it does this is by
        first parsing digits until it doesn't see any digits, and saving that result.
        Then parsing the hashtag.
        Then taking that many chars from the string, and adding it to the list of strings.
        And then advancing the string by that much.
        """
        strs = []

        while s:
            num, num_len = self.tok_number(s)
            s = s[num_len:]
            self.tok_delimiter(s)
            s = s[1:]
            parsed = self.take_chars(num, s)
            s = s[num:]
            strs.append(parsed)

        return strs

    def tok_delimiter(self, s: str):
        if s[0] != "#":
            raise RuntimeError("The character was not a #")

    def tok_number(self, s: str) -> tuple[int, int]:
        num = []
        for c in s:
            if c.isdigit():
                num.append(c)
            else:
                break
        return (int("".join(num)), len(num))

    def take_chars(self, n: int, s: str) -> str:
        return s[:n]


# Your Codec object will be instantiated and called as such:
def test():
    assert 2 + 2 == 4
