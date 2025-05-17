# 124. Binary Tree Maximum Path Sum

## 📝 Problem
Giving a `root`, we have to find a path from this tree to find a maximum total path sum.


### **Solution**:
- Recursive & Tree Concept
---

## 💡 Example

### **Example 1**:

**Input:**
```python
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```


### **Code** :
````python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val 

        def helper(root):
            nonlocal ans
            if not root:
                return 0
            left = max(helper(root.left),0)
            right= max(helper(root.right),0)
            ans = max(ans,root.val + left + right)
            return root.val + max(left,right)
        helper(root)
        return ans
        
`````