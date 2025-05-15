# 213. House Robber II

## 📝 Problem

Given a array `nums`, this problem, we have to solve how to get a lot of money but we get much money by robbing a house in array, but we cannot rob adjancent of array, example , we robbed the i, we cannot rob i+1, but we can rob i+2. But the new condition is , the array is cyclic.

### **Solution**:
- DFS + DP is the key of solution
---

## 💡 Example

### **Example 1**:
````
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
````
### **Code** :

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        memo =[[-1] * 2 for _ in range(len(nums))]

        def dfs(index, flag):
            if index >= len(nums) or flag and index == len(nums)-1:
                return 0
            if memo[index][flag]!= -1:
                return memo[index][flag]
            
            memo[index][flag] = max(dfs(index+1,flag), nums[index]+dfs(index+2, flag or (index==0)))
            return memo[index][flag]
        return max(dfs(0,True),dfs(0,False))
````
