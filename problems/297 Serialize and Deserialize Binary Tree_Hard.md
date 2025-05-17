# 297. Serialize and Deserialize Binary Tree

## 📝 Problem
Giving two function `encoder` and `decoder`, this problem requires you to make an encoder and then decoder it to be `tree`.


### **Solution**:
- Using dfs concept ,you can use post order , inorder or so on.
---

## 💡 Example

### **Example 1**:

**Input:**
```python
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```


### **Code** :
````python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res =[]

        def dfs(root):
            if not root:
                res.append("N")
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ".".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        value = data.split(".")
        index = 0

        def dfs():
            nonlocal index
            if value[index]=="N":
                index +=1
                return None
            node = TreeNode(int(value[index]))
            index +=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
`````