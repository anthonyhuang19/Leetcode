# 377 Combination Sum IV

## 📝 Problem

Giving an array `nums` , this problem want us to think that the value of array can be divided by two subset with the same total, for example : array A and array B is subset of array nums, means that A + B = nums , but total total(A) == total(b).

### **Solution**:

- Dynamic Programming & DFS -> Easy to appraoch because imagine you can use dfs to approach it and using memo for saving memory.(Make it simple)

---

## 💡 Example

### **Example 1**:

```python
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```
### **Code** :

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) 
        target = total //2 
        # Base case 
        if total % 2 != 0:
            return False
        memo ={}

        def dfs(i, target):
            if target == 0:
                return True
            if (i,target) in memo:
                return memo[(i,target)]
            if i >= len(nums) or target < 0:
                return False
            # Skip + not skip
            memo[(i,target)] = dfs(i+1,target) or dfs(i+1,target-nums[i])
            return memo[(i,target)]
        return dfs(0,target)
    # Time complexity:O(N * target), Space Time:O(N * target)
```


