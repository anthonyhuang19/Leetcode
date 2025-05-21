# 767. Reorganize String

## 📝 Problem
You are given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

### **Solution**:
- Using HashMap

---

## 💡 Example

### **Example 1**:
```
Input: s = "axyy"
Output: "xyay"
```
### **Code** :

```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        # So this problem requires us to rearrange the string without any same 
        # char in adja 
        freq = Counter(s)

        if max(freq.values()) > (len(s)+1)//2:
            return ""
        
        max_heap = [(-count,char) for char,count in freq.items()]
        heapq.heapify(max_heap)
        result =[]
        prev_count,prev_char = 0,""
        while max_heap:
            count,char = heapq.heappop(max_heap)
            result.append(char)

            if prev_count < 0:
                heapq.heappush(max_heap,(prev_count,prev_char))
            prev_count,prev_char = count +1,char
        return ''.join(result)
```