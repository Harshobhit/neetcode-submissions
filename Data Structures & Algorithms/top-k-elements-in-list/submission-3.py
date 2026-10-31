class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        freq_count = {}
        result = []

        for num in nums:
            freq_count[num] = 1 + freq_count.get(num, 0)
        
        for num, count in freq_count.items():
            bucket[count].append(num)
        
        
        print(bucket)
        for index in range(len(bucket)-1, 0, -1):
            for num in bucket[index]:
                result.append(num)
                if len(result) == k:
                    return result
        
       