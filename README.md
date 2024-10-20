# build_min_heap_from_scratch
write a min_heap and a heapify algorithm in Python from scratch, help to strengthen the understanding of heap and heapify.

## Introduction
A **Min-Heap** is a **nearly complete** binary tree where the value of each node is less than or equal to its child nodes. 
**Nearly complete** means that all levels are fully filled except possibly the last, as the tree is filled from left to right.

## Step 1:Define the Min-Heap Class
Start by defining a class `MinHeap` that will store the heap and provide operations for inserting elements and maintaining the heap property.
```python3
class MinHeap:
    def __init__(self):
        self.heap = []
```
## Step 2: Insert
Every time you insert an item/value, call heapify_up() to maintain the min_heap property.
```python3
def insert(self, value):
    self.heap.append(value)
    self.heapify_up(len(self.heap) - 1)
```
## Step 3: Heapify_up
Here is an assumption, that before inserting the element, the heap already satisfies the min_heap property, so we just need to check the new element and its ancestors(parents)to restore the min-heap property. And this process is done by **Heapify_up**, why? Because the newly inserted element is placed at the end of the heap, and all elements above it(closer to the root) already follow the min-heap property, the only possible violation of the heap property can happen between the newly inserted element and its parent. By recursively heapify_up, we can stop once the heap property is restored.
```python3
def heapify_up(self, index):
    if index == 0:
        return
    parent = (index - 1) // 2
    if self.heap[parent] > self.heap[index]:
        self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
        self.heapify_up(parent)
```
## Step 4: Delete the smallest or extract_min
In a MinHeap, the root element is always the smallest, when we try to pop the smallest element, we swap it with the last element in the min-heap first, and then execute pop to delete the smallest element.
```python3
def extract_min(self):
    if not self.heap:
        return None
    if len(self.heap) == 1:
        return self.heap.pop()

    min_ele = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.heapify_down(0)
    return min_ele
```
## Step 5: Heapify_down
After deleting the smallest element, we have a new element from the previous bottom at the root position, so we need to maintain the min_heap property by comparing the current root with its children and moving the smallest child up if necessary. And we'll do it recursively.
```python3
def heapify_down(self, parent):
    smallest = parent
    left_child = parent * 2 + 1
    right_child = parent * 2 + 2

    if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
        smallest = left_child
    if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
        smallest = right_child

    if smallest != parent:
        self.heap[parent], self.heap[smallest] = self.heap[smallest], self.heap[parent]
        self.heapify_down(smallest)
```
## Step 6: Get the smallest element not deleting
```python3
def get_min(self):
    if not self.heap:
        return None
    return self.heap[0]
```
## Step 7: Testing the min-heap I build
```python3
heap = MinHeap()
heap.insert(8)
print(f'Min element: {heap.extract_min()}')
heap.insert(4)
print(f'Min element: {heap.get_min()}')
heap.insert(5)
print(f'Min element: {heap.extract_min()}')
heap.insert(3)
print(f'Min element: {heap.extract_min()}')
heap.insert(10)
print(f'Min element: {heap.extract_min()}')
heap.insert(4)
print(f'Min element: {heap.get_min()}')
```
