# 343 Integer Break

## 📝 Problem

The Tribonacci sequence `Tn` is defined as follows: 

`T0 = 0, T1 = 1, T2 = 1`, and` Tn+3` = `Tn + Tn+1 + Tn+2` for` n >= 0`.

Given `n`, return the value of `Tn`

### **Solution**:

- Dynamic Programming & DFS -> Easy to appraoch because imagine you can use dfs to approach it and using memo for saving memory.(Make it simple)

---

## 💡 Example
**Input:**

```python
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

### **Code** :

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        memo ={0:0,1:1,2:1}

        def dfs(nums):
            if nums in memo:
                return memo[nums]
            
            memo[nums] = dfs(nums-1) + dfs(nums-2) +dfs(nums-3)
            return memo[nums]
        return dfs(n)
```