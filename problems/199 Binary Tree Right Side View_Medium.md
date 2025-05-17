# 450. Delete Node in a BST

## 📝 Problem

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

### **Solution**:

- BFS

---

## 💡 Example

### **Example 1**:

**Input:**

```python
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

## **Code**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []

        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size-1:
                    res.append(node.val)
                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
```
