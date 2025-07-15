# LeetCode 49. Group Anagrams

---

## 1. Problem Description

### Description:
Given an array of strings, group anagrams together.

---

### Input:
- A list of strings `strs` where 0 <= len(strs) <= 10^4 and 0 <= len(strs[i]) <= 100.

---

### Output:
- A list of groups of anagrams.

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
Input: strs = ["a"]
Output: [["a"]]
```

**Test Case 2:**
```
Input: strs = ["rat","tar","art"]
Output: [["rat","tar","art"]]
```

</details>

---

## 2. Approach

We use a dictionary to store the signature of each string where the signature is a tuple of the counts of each character in the string. If two strings have the same signature, they are anagrams. We iterate through each string, create its signature, and check if we have seen that signature before.

1. Initialize an empty dictionary `seen_dict` to store signatures and their corresponding index in result list.
2. Initialize an empty list `res` to store groups of anagrams.
3. Initialize `res_index` to keep track of the index in result list.
4. Iterate through each string in the input list:
   - Create a signature by counting the occurrences of each character in the string.
   - Convert the signature to a tuple for hashability.
   - If the signature is seen before, add the string to the corresponding group in the result list.
   - Else, store the signature in `seen_dict` with its index in the result list and create a new group in the result list.
5. Return the list of groups of anagrams.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(N * K) where N is the number of strings in the input list and K is the maximum length of a string in the list.
- **Space Complexity:** O(N * K) for the dictionary and the result list.