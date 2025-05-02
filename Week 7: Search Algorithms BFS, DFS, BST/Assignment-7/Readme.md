# Algorithm Problems 

## 1.Lowest Common Ancestor of a Binary Tree

### Problem Description
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

### Example

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


### Visual Explanation
![LCA](images/6-1.png)

![LCA](images/6-2.png)

---

## 2.  Top K Frequent Elements

### Problem Description
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
 
### Example
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

### Visual Explanation
![TopK](images/6-3.png)

![TopK](images/6-4.png)
---

## 3.Word Break

### Problem Description
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
### Example
Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

### Visual Explanation
![Word Break](images/6-5.png)

![Word Break](images/6-6.png)
---


