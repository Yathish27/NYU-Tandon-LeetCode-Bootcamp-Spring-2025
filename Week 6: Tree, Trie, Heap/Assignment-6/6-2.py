from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):

        freq_map = Counter(nums)

        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num)) 
            if len(heap) > k:
                heapq.heappop(heap)  

        result = [num for freq, num in heap]
        return result
