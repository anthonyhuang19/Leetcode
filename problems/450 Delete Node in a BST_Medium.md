# 450. Delete Node in a BST

## 📝 Problem
Basically, the deletion can be divided into two stages:
- Search for a node to remove.
- If the node is found, delete the node.


### **Solution**:
- Iteration O(h)

---

## 💡 Example

### **Example 1**:


**Input:**
```python
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val :
            root.right = self.deleteNode(root.right,key)
        elif key < root.val :
            root.left = self.deleteNode(root.left,key)
        else :
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val 
            root.right = self.deleteNode(root.right,root.val)
        return root
````


