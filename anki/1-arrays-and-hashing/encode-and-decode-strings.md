# 271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}

Machine 2 (receiver) has the function:

vector<string> decode(string s) {
  //... your code
  return strs;
}

So Machine 1 does:

string encoded_string = encode(strs);

and Machine 2 does:

vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:

Input: dummy_input = [""]
Output: [""]

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] contains any possible characters out of 256 valid ASCII characters.

Follow up: Could you write a generalized algorithm to work on any possible set of characters?

%

To solve this problem, we can first encode the strings by following the
format "{len(str)}#{str}". We do this to all the strings provided and
send it over as one string.

When decoding, we decode the strings by tokenizing them.
First, we keep tokenizing numbers until there aren't any more, and then
recreate the length of the string.
Second, we consume the hashtag (which delimits the end of the length).
Finally, we take the next `n` chars, where `n` is the length of the
string.

We repeat this for all the strings until we get our final result.

```python
class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
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
```
