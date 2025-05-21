# 1094. Car Pooling

## 📝 Problem
Giving `trips` and `capacity`, so we want to know that these trips can be implemented, cuz there are a limit in capacity.

### **Solution**:
- Using HashMap

---

## 💡 Example

### **Example 1**:
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```
### **Code** :

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        map =[0] * 1001 #1 <= trips.length <= 1000

        for i in trips:
            num,start,end = i
            map[start] +=num
            map[end] -=num
        curr = 0
        for i in range(1001):
            curr += map[i]
            if curr > capacity:
                return False
        return True
# Time complexity :O(N) where N = 1001
```