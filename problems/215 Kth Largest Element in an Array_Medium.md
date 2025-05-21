# 215. Kth Largest Element in an Array

## 📝 Problem
Given an integer array nums and an integer k, return the kth largest element in the array.Note that it is the kth largest element in the sorted order, not the kth distinct element.Can you solve it without sorting?

### **Solution**:
- Using HashMap

---

## 💡 Example

### **Example 1**:
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```
### **Code** :

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap =[]
        for value in nums:
            heapq.heappush(minheap,value)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]
````