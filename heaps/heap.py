class heap:
    def __init__(self):
        self.heap = []
    
    def _insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)
    
    def _get_min(self):
        return self.heap[0] if len(self.heap) > 0 else None
    
    def _siftup(self, i):
        parent = (i - 1) // 2
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2
    
    def _siftdown(self, i):
        left = 2*i+1
        right = 2*i+2
        while (
            left < len(self.heap) and self.heap[i] > self.heap[left] or
            right < self.heap and self.heap[i] > self.heap[right]
        ):
            if right >= len(self.heap) or self.heap[left] < self.heap[right]:
                smallest = left
            else:
                smallest = right

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            left = 2*i+1
            right = 2*i+2
    
            
