# 647 Palindromic Substring

## 📝 Problem

Giving an string `s` , return number of palindromic substring.

### **Solution**:
- Not optimal but i think the easy way to solve this problem , similar context of leetcode 5 
---

## 💡 Example

### **Example 1**:
````
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
````
### **Code** :

```python
class Solution:
    class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(left,right):
            ans = 0
            while left >=0 and right < len(s) and s[left]==s[right]:
                left-=1
                right+=1
                ans +=1
            return ans 
        res=0
        for i in range(len(s)):
            res += helper(i,i)
            res += helper(i,i+1)
        return res
        
````
