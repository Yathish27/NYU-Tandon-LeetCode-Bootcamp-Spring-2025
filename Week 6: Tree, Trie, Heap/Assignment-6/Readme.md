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

## 3. Number of People Aware of a Secret

### Problem Description
On day 1, one person discovers a secret.

You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.

Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.

### Example
Input: n = 6, delay = 2, forget = 4
Output: 5


### Visual Explanation
![Number of People Aware of a Secret](images/6-5.png)

![Number of People Aware of a Secret](images/6-6.png)
---


