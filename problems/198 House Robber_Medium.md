# 198. House Robber

## 📝 Problem

Given a array `nums`, this problem, we have to solve how to get a lot of money but we get much money by robbing a house in array, but we cannot rob adjancent of array, example , we robbed the i, we cannot rob i+1, but we can rob i+2.

### **Solution**:
- DFS + DP is the key of solution
---

## 💡 Example

### **Example 1**:
````
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
````
### **Code** :

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo ={}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return memo[i]
        return dfs(0)  
````
