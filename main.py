class Solution(object):
    """
    :type s: str
    :rtype: int
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest: int = 0

        for i, _ in enumerate(s):
            for j, _ in enumerate(s[i:], start=i):
                substring: str = s[i:j+1]
                seen: set[char] = set()

                is_unique: bool = True
                for char in substring:
                    if char in seen:
                        is_unique = False
                        break
                    seen.add(char)

                if is_unique:
                    longest = max(longest, len(substring))

        return longest
