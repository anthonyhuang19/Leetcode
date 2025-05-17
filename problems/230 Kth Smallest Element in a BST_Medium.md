# 230. Kth Smallest Element in a BST

## 📝 Problem
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


### **Solution**:

- Using inorder , from low variable to high variable.

---

## 💡 Example

### **Example 1**:

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

### **Code** :

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # using inorder
        arr =[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return arr[k-1]
```
