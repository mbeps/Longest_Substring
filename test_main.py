import pytest
from main import Solution 

solution = Solution()

def test_lengthOfLongestSubstring_abcabcbb():
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3

def test_lengthOfLongestSubstring_bbbbb():
    assert solution.lengthOfLongestSubstring("bbbbb") == 1

def test_lengthOfLongestSubstring_pwwkew():
    assert solution.lengthOfLongestSubstring("pwwkew") == 3

def test_lengthOfLongestSubstring_empty():
    assert solution.lengthOfLongestSubstring("") == 0

def test_lengthOfLongestSubstring_space():
    assert solution.lengthOfLongestSubstring(" ") == 1

def test_lengthOfLongestSubstring_au():
    assert solution.lengthOfLongestSubstring("au") == 2

def test_lengthOfLongestSubstring_aab():
    assert solution.lengthOfLongestSubstring("aab") == 2

def test_lengthOfLongestSubstring_dvdf():
    assert solution.lengthOfLongestSubstring("dvdf") == 3

def test_lengthOfLongestSubstring_anviaj():
    assert solution.lengthOfLongestSubstring("anviaj") == 5

def test_lengthOfLongestSubstring_none():
    with pytest.raises(TypeError):
        solution.lengthOfLongestSubstring(None)
