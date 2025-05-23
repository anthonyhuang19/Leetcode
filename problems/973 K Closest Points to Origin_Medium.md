# 1834. Single-Threaded CPU

## 📝 Problem
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

### **Solution**:
- Using HashMap

---

## 💡 Example

### **Example 1**:
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```
### **Code** :

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        array = []

        for x,y in points:
            dist = (x**2) + (y**2)
            dist = math.sqrt(dist)
            array.append((dist,x,y))
        heapq.heapify(array)
        res = []
        while k > 0:
            dist,x,y = heapq.heappop(array)
            res.append((x,y))
            k -=1
        return res
        
````