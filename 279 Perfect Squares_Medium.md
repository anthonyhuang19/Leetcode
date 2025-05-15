# 279 Perfect Squares

## 📝 Problem

Giving ```n``` , this problem want to return the least number of perfect square that can sum all the total to ```n```.

### **Solution**:

- Dynamic Programming & DFS -> Easy to appraoch because imagine you can use dfs to approach it and using memo for saving memory.(Make it simple)

---

## 💡 Example

### **Example 1**:
```
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
```
### **Code** :

```python
class Solution:
    def numSquares(self,n):
        memo ={}

        def dfs(num):
            if num == 0:
                return 0 
            if num in memo:
                return memo[num]

            res = num
            for i in range(1,num+1):
                if i * i > num:
                    break 
                res = min(res, 1 + dfs(num-i*i))
            memo[num]= res
            return res
        return dfs(n)
```