class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq_count = {}
        for num in nums:
            if num in freq_count:
                freq_count[num] += 1
            else:
                freq_count[num] = 1
        
        heap = []
        for num, count in freq_count.items():
            heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
        
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result