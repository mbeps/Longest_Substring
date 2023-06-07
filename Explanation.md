# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This problem is about finding the longest substring without repeating characters. To approach this, we'll utilize a "sliding window" technique due to its efficiency. 

The sliding window algorithm is a technique for solving problems on sequences of data. It works by maintaining a window of fixed size over the data, and then moving the window over the data one element at a time. The algorithm then performs a computation on the data within the window, and then moves the window on to the next element. This process is repeated until the entire data sequence has been processed.

# Approach
<!-- Describe your approach to solving the problem. -->
The sliding window technique involves using two pointers to keep track of the current "window" in the string that we're looking at. In our case, the left pointer (`left`) represents the beginning of the current substring we're considering, and the right pointer (`right`) represents the end. 

**Steps:**
1. Initialize an empty dictionary `seen` to store the most recent index at which we've seen each character.
2. Initialize `left` and `longest` to 0.
3. Loop over the string with the index and character.
   - If the character has not been seen before, store the index in the `seen` dictionary.
   - If the character has been seen and its previous occurrence is inside the current window (i.e., `seen[char] >= left`), we move the left pointer to the right of the previous occurrence to avoid repetition in the window. We also update the new index of the current character.
   - Update the length of the longest substring seen so far (`longest`) if the length of the current window (`right - left + 1`) is greater.

# Complexity
- Time complexity: $$O(n)$$, where $$n$$ is the length of the string. This is because we are traversing the string once.
- Space complexity:  $$O(k)$$, where $$k$$ is the size of the dictionary. In the worst case, this will be the size of the input string, i.e., $$O(n)$$, when all characters are distinct. However, if we consider the fact that the number of distinct characters is likely to be limited (for example, the number of ASCII characters is 128), then this can also be considered as $$O(1)$$.

# Code
```py
class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    seen = {}
    left = 0
    longest = 0

    for right, char in enumerate(s):
      if char not in seen:
          seen[char] = right
      else:
          if seen[char] >= left:
              left = seen[char] + 1
          seen[char] = right
      
      longest = max(longest, right - left + 1)
    return longest
```

**Type Hinted**
```py
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
```