# 746. Min Cost Climbing Stairs

## 📝 Problem
Giving a array```cost```, This question requires us to find the minimum cost to pass throught the stairs.
### **Solution**:
- Dynamic Programming & DFS -> Easy to appraoch because imagine you can use dfs to approach it and using memo for saving memory.(Make it simple)
---

## 💡 Example

```python
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

### **Code** :
````python
class Solution:
    def tribonacci(self, n: int) -> int:
        memo ={0:0,1:1,2:1}

        def dfs(nums):
            if nums in memo:
                return memo[nums]
            
            memo[nums] = dfs(nums-1) + dfs(nums-2) +dfs(nums-3)
            return memo[nums]
        return dfs(n)
# Time Complexity:O(n) and Space time :O(n)
`````