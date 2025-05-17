# 98. Validate Binary Search Tree

## 📝 Problem
A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.

Both the left and right subtrees must also be binary search trees.


### **Solution**:

- Using recursive

---

## 💡 Example

### **Example 1**:

```
Input: root = [2,1,3]
Output: true
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,minValue,maxValue):
            if not root:
                return True 
            if minValue is not None and root.val <= minValue:
                return False
            if maxValue is not None and root.val >= maxValue:
                return False
            return helper(root.left,minValue,root.val) and helper(root.right,root.val,maxValue)
        return helper(root,None,None)
```
