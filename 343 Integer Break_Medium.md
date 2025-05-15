# 343 Integer Break

## 📝 Problem

Giving integer `n`, this problem want us to think how to break n into `k>=2` so that multiplication of `K1 * K2 and so on ` can get a maximum number or value

### **Solution**:

- Dynamic Programming & DFS -> Easy to appraoch because imagine you can use dfs to approach it and using memo for saving memory.(Make it simple)

---

## 💡 Example

### **Example 1**:

**Input:**

```python
n = 2
```

**Output**

```
1
```

**Explanation**

```
2 = 1 + 1 and 1 * 1 = 1 , this is the maximum number that we can calculate in n == 2.
```

### **Code** :

```python
class Solution:
    def integerBreak(self,n:int) -> int :
        # Base case
        memo = {1:1,2:1,3:2}

        def dfs(number):
            # checking number in memo or not
            if number in memo :
                return memo[number]
            # Finding the max_product by i * number - i or dfs to make i * a * b and so on
            res = 0
            for i in range(1,number):
                curr = i * max(number-i, dfs(number-i))
                res = max(res,curr)
            memo[number]=res
            return res
        return dfs(n)
```