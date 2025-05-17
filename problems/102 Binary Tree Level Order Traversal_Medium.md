# 450. Delete Node in a BST

## 📝 Problem

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

### **Solution**:

- BFS

---

## 💡 Example

### **Example 1**:

**Input:**

```python
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        q = collections.deque([root])
        ans = []
        while q :
            length = len(q)
            temp = []
            for i in range(length):
                node = q.popleft()
                temp.append(node.val)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            ans.append(temp)
        return ans


```
