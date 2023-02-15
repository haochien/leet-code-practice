from typing import List
from collections import Counter
from heapq import heapify, heappop

class TopKFrequentElement:
    """
    LeetCode Question Nr.347
    https://leetcode.com/problems/top-k-frequent-elements/

    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order.
    It is guaranteed that the answer is unique.

    Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Example 2:
    Input: nums = [1], k = 1
    Output: [1]
    """

    @staticmethod
    def great_ans1(nums: List[int], k: int) -> List[int]:
        """
        technique: hash / bucket sort
        Time: O(n)
        Memory: O(n)
        https://www.youtube.com/watch?v=YPTqKIgVk-k
        """
        count = {}
        freq = [[] for i in range(len(nums)+1)]  # buckets for count 0, 1, 2, 3, ... len(nums) 

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for k, v in count.items():
            freq[v].append(k)
        
        res = []
        for i in range(len(freq)-1, 0, -1):  # bucket 0 will never have anything, so the last of range is bucket 1
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    @staticmethod
    def great_ans2(nums: List[int], k: int) -> List[int]:
        """
        technique: Max Heap
        Time: O(N + KlogN): heapify(maxHeap) costs O(N) ; heappop(maxHeap) k times costs O(KlogN)
        Memory: O(n)
        https://leetcode.com/problems/top-k-frequent-elements/solutions/1502514/c-python-2-solutions-maxheap-bucket-sort-clean-concise/

        note:
        Counter: https://realpython.com/python-counter/
        Heap: https://www.tutorialspoint.com/python_data_structure/python_heaps.htm
        """
        cnt = Counter(nums)
        maxHeap = [[-freq, num] for num, freq in cnt.items()]
        heapify(maxHeap)
        
        ans = []
        for i in range(k):
            _, num = heappop(maxHeap)
            ans.append(num)
        return ans


    @staticmethod
    def my_solution(nums: List[int], k: int) -> List[int]:
        """
        Time: O(nlogn)
        Memory: O(n)
        """
        
        hash = {}

        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1

        lst_max_k = sorted(list(hash.values()))[-1:-k-1:-1]

        res = []
        for k, v in hash.items():
            if v in lst_max_k:
                res.append(k)

        return res


