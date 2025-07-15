# LeetCode [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

---

## 1. Problem Description

### Description:
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order. An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

### Input:
A list of strings `strs`, where
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

### Output:
A list of lists of strings, where each sublist contains all the strings from `strs` that are anagrams of each other. The order of the groups and the order of the strings within a group does not matter.

---

### Example(s):
**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```
Input: strs = []
Output: []
Explanation: Empty input yields no groups.
```

**Test Case 2:**
```
Input: strs = ["a"]
Output: [["a"]]
Explanation: Single-element list forms one group.
```

</details>

---

## 2. Approach

We use a **Hash Map** keyed by a letter‐count signature to group anagrams.

1. Initialize an empty dictionary `seen_dict` that maps a signature tuple → index in result list.
2. Initialize an empty list `res` to hold the groups.
3. Iterate through each string in `strs`:
   - Build a length-26 array `signature` to count occurrences of each letter (`'a'` to `'z'`).
   - Convert this array to a tuple `hashable_signature` so it can be used as a dictionary key.
   - If `hashable_signature` exists in `seen_dict`, append the current string to the corresponding sublist in `res`.
   - Otherwise, record a new group:
     - Map `hashable_signature` → next `res` index.
     - Append a new sublist containing the current string to `res`.
4. Return `res`.

Why this solution?
- Counting letters avoids sorting each string (O(K log K)) and runs in O(K) per string.
- Hashing the fixed-size 26-length tuple is O(1) on average.

Patterns used: Hashing, Counting Sort for fixed alphabet.

Alternative:
- Sort each string as a key (O(K log K) per string), then group by sorted string.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(N · K), where N = number of strings, K = maximum length of a string.  
  (Counting letters and tuple conversion take O(K). Dictionary operations are O(1) on average.)
- **Space Complexity:** O(N · K), to store the signatures and the output groups.