# 1834. Single-Threaded CPU

## 📝 Problem
You are given `n`​​​​​​ tasks labeled from `0` to `n - 1` represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

### **Solution**:
- Using HashMap

---

## 💡 Example

### **Example 1**:
```
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
```
### **Code** :

```python
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(et,pt,i) for i,(et,pt) in enumerate(tasks)]
        tasks.sort()
        i = time = 0
        result = []
        min_heap=[]
        n = len(tasks)
        
        while i < n or min_heap:
            if not min_heap and time < tasks[i][0]:
                time = tasks[i][0]
            while i < n and tasks[i][0] <= time :
                et,pt,index = tasks[i]
                heapq.heappush(min_heap,(pt,index))
                i +=1
            if min_heap:
                pt,index = heapq.heappop(min_heap)
                time += pt 
                result.append(index)
        return result
```