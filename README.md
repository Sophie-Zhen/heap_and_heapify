# min_heap_from_scratch
write a min_heap and a heapify algorithm in Python from scratch, help to strengthen the understanding of heap and heapify.

## Introduction
A **Min-Heap** is a **nearly complete** binary tree where the value of each node is less than or equal to its child nodes. 
**Nearly complete** means that all levels are fully filled except possibly the last, as the tree is filled from left to right.

## Step 1:Define the Min-Heap Class
Start by defining a class `MinHeap` that will store the heap and provide operations for inserting elements and maintaining the heap property.
```python
class MinHeap:
    def __init__(self):
        self.heap = []
```
## Step 2: 
