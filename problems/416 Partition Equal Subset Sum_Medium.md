# 377 Combination Sum IV

## 📝 Problem

Giving an array `nums` and ```target```, this problem want to us to find a way or how many way to make element in array can be sum up that is same as target.

### **Solution**:

- Dynamic Programming & DFS -> Easy to appraoch because imagine you can use dfs to approach it and using memo for saving memory.(Make it simple)

---

## 💡 Example

### **Example 1**:

```python
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
```
### **Code** :

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo ={0:1}
        
        def dfs(target):
            if target in memo:
                return memo[target]
            res = 0 
            for i in nums:
                if i > target : 
                    break 
                res += dfs(target-i)
            memo[target]= res
            return memo[target]
        return dfs(target)
```


