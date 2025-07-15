# Problem '49'

## 1. Problem Description

### Description:

Given an array of strings, group anagrams together. An anagram is a word formed by rearranging the letters of a different word, using all the original letters exactly once.

---

### Input:

* `strs`: A list of strings where each string consists of lowercase English letters.

---

### Output:

* A list of lists where each inner list contains strings that are anagrams of each other.

---

### Example(s):

**Example 1:**
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
```

**Example 2:**
```
Input: ["listen", "silent", "enlist"]
Output: [["listen","silent"],["enlist"]]
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```
Input: ["race", "care", "acre"]
Output: [["race"],["care","acre"]]
```

**Test Case 2:**
```
Input: ["abc", "def", "ghi"]
Output: [["abc"],["def"],["ghi"]]
```

</details>

---

## 2. Approach

The solution uses a **Hash Table Approach**:

* Create a dictionary `seen_dict` to store unique anagram signatures.
* Iterate through each string in the input list:
    * Create a signature for each string by counting the frequency of each letter.
    * Convert the signature to a hashable tuple.
    * If the signature is already in `seen_dict`, append the string to the corresponding list in the result.
    * If the signature is not in `seen_dict`, add it to the dictionary with a new index in the result list.
* Return the final result list.

This approach efficiently groups anagrams together based on their signature.

---

## 3. Algorithm Complexity

* **Time Complexity:** O(n * m), where n is the number of strings in the input list and m is the average length of a string. The time complexity is dominated by iterating through each character in each string.
* **Space Complexity:** O(n), where n is the number of unique anagram signatures in the input list.

--- 

By following this README, users can understand the problem, the implemented solution, and its complexity, making it easier to utilize or modify the code for their needs.