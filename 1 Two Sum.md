# 1. Two Sum Problem

## 📝 Problem

Given an array of integers `nums` and an integer `target`, find **two distinct indices** such that the numbers at those indices add up to the `target`. There is exactly **one solution**, and you cannot use the same element twice.

### **Solution**:
- Brute Force
- The best option is using Map or Hash Map in Python

---

## 💡 Example

### **Example 1**:

**Input:**
```python
nums = [2, 7, 11, 15]
target = 9
```
**Output**
```
[0,1]
```

### **Code** :
````python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for index,number in enumerate(nums):
            temp = target - number
            if temp in count :
                return [count[temp],index]
            count[number] = index
        return [-1,-1]
`````

Time  Complexity is O(n) and Space time :O(n)
