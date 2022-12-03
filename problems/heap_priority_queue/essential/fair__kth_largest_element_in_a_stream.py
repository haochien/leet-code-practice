from typing import List
import heapq

class KthLargestInStream:
    """
    LeetCode Question Nr.703
    https://leetcode.com/problems/kth-largest-element-in-a-stream/

    Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Implement KthLargest class:

    - KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    - int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

    ["KthLargest", "add", "add", "add", "add", "add"]
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output
    [null, 4, 5, 5, 8, 8]

    Explanation
    KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3);   // return 4
    kthLargest.add(5);   // return 5
    kthLargest.add(10);  // return 5
    kthLargest.add(9);   // return 8
    kthLargest.add(4);   // return 8
    """

    @staticmethod
    class GreatAns1:
        """
        technique: Min Heap of Size K
        Time: O((n-k)logn) 
              --> when initiate class, it needs (n-k) times popping. So the worst case the big O will be nlogn
              --> more accurate is M * nlogn, M is determined by how many numbers you are going to add
        https://www.youtube.com/watch?v=hOjcdrqMoQ8

        Note:
        Heap is a special tree structure in which each parent node is less than or equal to its child node. Then it is called a Min Heap.
        If each parent node is greater than or equal to its child node then it is called a max heap.
        https://www.tutorialspoint.com/python_data_structure/python_heaps.htm

        binary heap vs sorted:
        If you use binary heap to pop all elements in order, the thing you do is basically heapsort. It is slower than sort algorightm in sorted function.
        The heapq is faster than sorted in case if you need to add elements on the fly.
        The sorted is faster if you will need to retrieve all elements in order later.
        https://stackoverflow.com/questions/24666602/python-heapq-vs-sorted-complexity-and-performance

        add & pop in heap is O(logn), and can get min from the heap in O(1) time
        In this question, we only add element, not drop element from list. So minHeap with size k largest is a good solution
        
        """
        def __init__(self, k: int, nums: List[int], nums_to_be_added: List[int]):
            self.kth = k
            self.min_heap = nums
            self.lst_num_added = nums_to_be_added

            heapq.heapify(self.min_heap) # convert list to min Heap structure
            while len(self.min_heap) > k:
                heapq.heappop(self.min_heap)  # using pop to leave only kth largest elements in the heap

        def add(self, val: int) -> int:
            heapq.heappush(self.min_heap, val)
            while len(self.min_heap) > self.kth:
                heapq.heappop(self.min_heap)

            return self.min_heap[0]
        
        def execute(self):
            lst_result = [None]
            for i in self.lst_num_added:
                lst_result.append(self.add(i))
            
            return lst_result


    class MySolution:
        """
        technique: Sort
        Time: O(n * nlogn) --> appending causes O(n) and sorted cause n(logn)
        """
        def __init__(self, k: int, nums: List[int], nums_to_be_added: List[int]):
            self.kth = k
            self.lst_targets = nums
            self.lst_num_added = nums_to_be_added

        def add(self, val: int) -> int:
            self.lst_targets.append(val)
            self.lst_targets = sorted(self.lst_targets, reverse=True)

            return self.lst_targets[self.kth-1]
        
        def execute(self):
            lst_result = [None]
            for i in self.lst_num_added:
                lst_result.append(self.add(i))
            
            return lst_result
    






