# 450. Delete Node in a BST

## 📝 Problem

Given the `array`,we need to construct Quad Tree.

### **Solution**:

- dfs

---

## 💡 Example

### **Example 1**:

**Input:**

```python
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
```

## **Code**

```python
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,r,c):
            if n == 1:
                return Node(grid[r][c]==1,True)

            mid = n //2
            topleft = dfs(mid,r,c)
            topright = dfs(mid,r,c+mid)
            bottomleft = dfs(mid,r+mid,c)
            bottomright= dfs(mid,r+mid,c+mid)

            if (topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and
                topleft.val == topright.val == bottomleft.val == bottomright.val):
                return Node(topleft.val,True)
            return Node(False,False,topleft,topright,bottomleft,bottomright)
        return dfs(len(grid),0,0)
```
