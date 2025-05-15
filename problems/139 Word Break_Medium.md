# 139 Word Break

## 📝 Problem

Giving an string `s` and an wordDictionary `WordDict` , this question need us to find "Is it possible for us to create string `s` from `worddict`, answer `True` or `False`.

### **Solution**:

- Dynamic Programming & DFS -> Easy to appraoch because imagine you can use dfs to approach it and using memo for saving memory.(Make it simple)

---

## 💡 Example

### **Example 1**:

````python
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
````
### **Code** :

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo ={len(s):True}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        memo[i] = True
                        return True 
            memo[i] = False
            return False
        return dfs(0)
````
