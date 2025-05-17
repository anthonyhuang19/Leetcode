# 1325. Delete Leaves With a Given Value

## 📝 Problem

Giving `root` and `target`, root is a tree and then `target`is integere, so we have to delete a leaf that is similar with `target`.

### **Solution**:

- Using `recursive `(post-order).

---

## 💡 Example

### **Example 1**:
```
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
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
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root :
            return None 
        
        # Left -> right  -> node 
        root.left = self.removeLeafNodes(root.left,target)
        root.right= self.removeLeafNodes(root.right,target)

        if not root.left and not root.right and root.val == target:
            return None
        return root
```