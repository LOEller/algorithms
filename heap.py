class MaxHeap:
    # a class to implement a max heap
    # ie a binary tree where any parent node
    # is larger than its children

    def __init__(self):
        self.heap = []

    def push(self, x):
        # inserts a new number into the heap

        # add the new element at the end of the heap
        self.heap.append(x)

        # if this will violate the heap property,
        # sift up the new element until the heap 
        # property has been reestablished 
        new_idx = len(self.heap)-1
        while new_idx > 0:
            parent_idx = (new_idx - 1) // 2
            if self.heap[new_idx] > self.heap[parent_idx]:
                self.heap[new_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[new_idx]
                new_idx = parent_idx
            else:
                break

    def pop(self):
        # removes the largest element from the heap
        # and returns it 

        if len(self.heap) == 0:
            return 
        
        if len(self.heap) == 1:
            return self.heap.pop()

        # remove the root and insert the last element of 
        # the heap in the root
        root = self.heap[0]
        self.heap[0] = self.heap.pop(-1)

        # If this will violate the heap property, 
        # sift down the new root to reestablish the heap property
        new_idx = 0
        while True:
            left_child_idx = 2 * new_idx + 1
            right_child_idx = 2 * new_idx + 2
            largest_idx = new_idx

            if left_child_idx < len(self.heap) and self.heap[left_child_idx] > self.heap[largest_idx]:
                largest_idx = left_child_idx
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] > self.heap[largest_idx]:
                largest_idx = right_child_idx
            
            if largest_idx != new_idx:
                self.heap[new_idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[new_idx]
                new_idx = largest_idx
            else:
                break

        return root
    

if "__main__" == __name__:
    heap = MaxHeap()
    for i in range(10):
        heap.push(i)

    for i in range(10):
        print(heap.pop())

