# 300 Longest Increasing Subsequence

## 📝 Problem

Giving an array `nums` , this problem want us to find the longest increasing subsequence, base on array.

### **Solution**:

- Dynamic Programming & DFS -> Easy to appraoch because imagine you can use dfs to approach it and using memo for saving memory.(Make it simple)

---

## 💡 Example

### **Example 1**:

````python
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
````
### **Code** :

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo ={}

        def dfs(i):
            if i in memo :
                return memo[i]
            res = 1
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    res = max(res,1+dfs(j))
            memo[i] = res
            return res

        return max(dfs(i) for i in range(len(nums)))
````
