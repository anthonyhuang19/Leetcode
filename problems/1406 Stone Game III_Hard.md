# 1406. Stone Game III

## 📝 Problem

Giving a array`stonevalue`, This question requires us to find the winner bob or alice where both of them have the same intelligent (only can take 3 stones from the first one ).

### **Explanation Solution**:

I think this problem is hard becuase we have to find a solution out of the box, but we can assume that bob is minus and alice is plus, if we get a plus we can say that alice win, and so on.

### **Solution**:

- Dynamic Programming & DFS -> Easy to appraoch because imagine you can use dfs to approach it and using memo for saving memory.(Make it simple)

---

## 💡 Example

```python
Input: stoneValue = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
```

### **Code** :

```python
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo ={}

        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            res, total = -math.inf, 0
            for j in range(i,min(i+3,len(stoneValue))):
                total += stoneValue[j]
                res = max(res, total - dfs(j+1))
            memo[i]= res
            return res
        result = dfs(0)
        if result == 0:
            return "Tie"
        return "Alice" if result > 0 else "Bob"
```
