# Algorithm Problems 

## 1.Implement Queue using Stacks

### Problem Description
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
### Example

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]



### Visual Explanation
![Implement Queue using Stacks](images/4-1.png)

![Implement Queue using Stacks](images/4-2.png)

---

## 2. Decode String

### Problem Description
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 
### Example
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"


### Visual Explanation
![Decode String](images/4-3.png)

![Decode String](images/4-4.png)
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
![Number of People Aware of a Secret](images/4-5.png)

![Number of People Aware of a Secret](images/4-6.png)
---


