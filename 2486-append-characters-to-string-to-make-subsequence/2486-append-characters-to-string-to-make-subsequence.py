class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first = 0
        longest_prefix = 0

        while first < len(s) and longest_prefix < len(t):
            if s[first] == t[longest_prefix]:
                # Since at the current position both the characters are equal,
                # increment longest_prefix by 1
                longest_prefix += 1
            first += 1

        # The number of characters appended is given by the difference in length of t
        # and longest_prefix
        return len(t) - longest_prefix