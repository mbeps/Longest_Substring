class Solution(object):
  def lengthOfLongestSubstring(self, s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    seen: dict[str, int] = {}
    left: int = 0
    longest: int = 0

    for right, char in enumerate(s):
      if char not in seen:
          seen[char] = right
      else:
          if seen[char] >= left:
              left = seen[char] + 1
          seen[char] = right
      
      longest = max(longest, right - left + 1)
    return longest