# 1448. Count Good Nodes in Binary Tree

## 📝 Problem

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.Return the number of good nodes in the binary tree.

### **Solution**:
- DFS
- BFS

---

## 💡 Example

### **Example 1**:


**Input:**
```python
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```
**Output**
```
[0,1]
```

### **Code** :
DFS :
````python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,maxNode):
            if not node :
                return 0
            res = 1 if node.val >= maxNode else 0
            maxNode = max(maxNode,node.val)
            res += dfs(node.left,maxNode)
            res += dfs(node.right,maxNode)
            return res
        return dfs(root,-math.inf)
`````

BFS :
````python
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0 
        res =0
        q = deque()
        q.append((root,-math.inf))

        while q :
            node,maxValue = q.popleft()
            if node.val >= maxValue:
                res +=1
            
            if node.left :
                q.append((node.left,max(node.val,maxValue)))
            if node.right :
                q.append((node.right,max(node.val,maxValue)))
        return res
````