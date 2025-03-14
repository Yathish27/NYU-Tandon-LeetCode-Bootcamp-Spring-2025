# Algorithm Problems 

This repository contains solutions algorithm problems, including **Two Sum II - Input Array Is Sorted**, **Product of Array Except Self**, and **Sort Colors**.
## 1.  String to Integer (atoi)

### Problem Description
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
### Example
Input: s = "42"
Output: 42



### Visual Explanation
![Two Sum II Visualization](images/2.1.png)

![Two Sum II Visualization](images/2.2.png)

---

## 2. Find All Anagrams in a String

### Problem Description
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

### Example
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]


### Visual Explanation
![Product of Array Except Self Visualization](images/2.3.png)

![Product of Array Except Self Visualization](images/2.4.png)
---

## 3.Reverse Words in a String

### Problem Description
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.
### Example
Input: s = "the sky is blue"
Output: "blue is sky the"



### Visual Explanation
![Sort Colors Visualization](images/2.5.png)

![Sort Colors Visualization](images/2.6.png)
---

