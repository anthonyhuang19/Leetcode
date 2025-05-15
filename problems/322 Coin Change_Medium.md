# 322 Coin Changes

## 📝 Problem

Giving an array `coins` and also `amount`, so from this problem, we have to find if it is possible from every coins element to sum up total == amount and finding the minimum number of coin that required.

### **Solution**:
- Using DFS + Memo (DP programming).
---

## 💡 Example

### **Example 1**:

````python
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
````
### **Code** :

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo ={}

        def dfs(target):
            if target == 0 :
                return 0
            if target in memo:
                return memo[target]
            res = math.inf
            for coin in coins:
                if target - coin >= 0:
                    res = min(res,1+dfs(target-coin))
            memo[target]=res
            return res 
        result = dfs(amount)
        return result if result != math.inf else -1
````
