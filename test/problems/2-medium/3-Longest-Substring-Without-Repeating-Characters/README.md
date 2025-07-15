# 3-Longest-Substring-Without-Repeating-Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

Example:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc", which has a length of 3.
```

## Approach
We can solve this problem using a sliding window approach. We will keep track of the current substring using a set to store the characters that we have seen so far. We will also maintain two pointers, `left` and `right`, to denote the current window.

1. Initialize an empty set `current_sub` to store characters in the current substring.
2. Initialize `left`, `right`, `max_length`, and `current_length` to 0.
3. Iterate through the string `s` using the `right` pointer.
4. If the character at `right` is not in `current_sub`, add it to `current_sub`, increment `current_length`, and update `max_length` if needed.
5. If the character at `right` is already in `current_sub`, remove the character at `left` from `current_sub`, move `left` pointer one position to the right, and decrement `current_length`.
6. Continue iterating until we reach the end of the string.
7. Return `max_length`, which is the length of the longest substring without repeating characters.

## Usage
1. Copy the `lengthOfLongestSubstring` function to your Python environment or file.
2. Call the function with a string input to find the length of the longest substring without repeating characters.

Example:
```python
print(lengthOfLongestSubstring("abcabcbb")) # Output: 3
```