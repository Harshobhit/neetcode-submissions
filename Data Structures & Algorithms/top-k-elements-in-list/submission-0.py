class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq_count = {}
        for num in nums:
            if num in freq_count:
                freq_count[num] += 1
            else:
                freq_count[num] = 1
        
        for num, count in freq_count.items():
            if count >= k:
                result.append(num)
        return result
