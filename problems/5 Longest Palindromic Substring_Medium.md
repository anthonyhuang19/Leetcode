# 5. Longest Palindromic Substring

## 📝 Problem

Given a string s, return the longest palindromic substring in s.

### **Solution**:
- Using concept of two pointer.
---

## 💡 Example

### **Example 1**:
````
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
````
### **Code** :

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right+=1
            return right-left-1
        
        
        length =0
        start = 0
        
        for i in range(len(s)):
            a = helper(i,i)
            b = helper(i,i+1)
            size = max(a,b)

            if length < size:
                length = size
                start = i - (size)//2
                if size % 2==0:
                    start +=1
        return s[int(start):int(start+length)]   
````
