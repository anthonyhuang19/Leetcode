# 91 Decode Way

## 📝 Problem

Giving an string `s` ,from this problem, we have to use dp programing to find the number of way to decode this string `s`.

### **Solution**:
- Using DFS + Memo (DP programming).
---

## 💡 Example

### **Example 1**:
````
Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).
````
### **Code** :

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        memo ={len(s):1}

        def dfs(i):
            if i in memo :
                return memo[i]
            if s[i] == "0":
                return 0
            
            # Skip until end of string
            res = dfs(i+1)
            # condition alphabet == 26 
            if (i+1 < len(s)) and (s[i] == "1" or (s[i]=="2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            memo[i]= res
            return res
        return dfs(0)      
````
