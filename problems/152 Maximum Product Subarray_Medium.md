# 152. Maximum Product Subarray

## 📝 Problem

Giving an array `nums`, this question requires us to find the largest possible product subarray from nums.

### **Solution**:
- Using kadane algorithm
---

## 💡 Example

### **Example 1**:

````python
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
````
### **Code** :

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmax = curmin =1

        for num in nums:
            temp = num * curmax
            curmax = max(num,curmin * num,temp)
            curmin = min(num,curmin * num,temp)
            res = max(res,curmax)
        return res
# Time Complexity :O(n) and space time :O(1)
````
