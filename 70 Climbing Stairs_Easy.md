# 70. Climbing Staris

## 📝 Problem
Giving a number of integer ```n```, imagine that you can only climb from level 0 to top by climbing 1 or 2 steps only. Question is hwo many distinct or the easy way to understand is how many way you can reach the top ?
### **Solution**:
- Dynamic Programming & DFS -> Easy to appraoch because imagine you can use dfs to approach it and using memo for saving memory.(Make it simple)
---

## 💡 Example

### **Example 1**:

**Input:**
```python
n = 2
```
**Output**
```
2
```
**Explanation**
```
There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

### **Code** :
````python
class Solution:
    def climbStairs(self,n :int)-> int:
        memo = {}

        def dfs(i):
            if i >= n:
                return i == n
            if i in memo :
                return memo[i]
            # Only 1 or 2 step 
            memo[i] = dfs(i+1) + dfs(i+2)
            return memo[i]
        return dfs(0)
`````

Time  Complexity is O(n) and Space time :O(n)
