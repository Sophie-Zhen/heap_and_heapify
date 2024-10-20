#define the class
class MinHeap:
    def __init__(self):
        self.heap = [] #initialize heap as a list

    def insert(self, value):
        self.heap.append(value)  #insert a value into the heap
        self.heapify_up(len(self.heap) - 1) #call heapify_up() to maintain the MinHeap property

    def heapify_up(self, index): #here is an assumption, that before inserting the element, the heap already satisfies the min_heap property
        if index == 0:
            return
        parent = (index - 1)//2
        if self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)

    def extract_min(self): #delete the smallest element
        if len(self.heap) == 0: #check if the heap is empty
            return None
        if len(self.heap) == 1: #check if the heap length is 1
            return self.heap.pop()
                    
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0] # swap the first(smallest) and the last element
        min_ele = self.heap.pop() #pop the last element(after swap is the smallest)
        self.heapify_down(0) #after popping the smallest, the new element is at the root position, we should call heapify_down from the root
        return min_ele

    def heapify_down(self, parent): # the key point is to understand the indexes between parent and left and right children
        smallest = parent
        left_child = parent * 2 + 1
        right_child = parent * 2 + 2
        #below: find the index of the smallest among parent, left_child and right_child, just update the index first
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        # when we find the smallest value and put smallest index at the smallest value(if not parent), we can swap it with the parent
        if smallest != parent:
            self.heap[parent], self.heap[smallest] = self.heap[smallest], self.heap[parent]
            self.heapify_down(smallest) # now the value of the original parent is at the index of smallest, we need to continue maintaining the min-heap property until the tree satisfies min-heap property

    def get_min(self):
        if not heap:
            return None
        return self.heap[0]


# Testing
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