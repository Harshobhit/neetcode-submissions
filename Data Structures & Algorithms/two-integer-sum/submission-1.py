class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        l = 0
        r = len(nums)-1

        while l<r:
            left_val, right_val = nums_sorted[l], nums_sorted[r]
            if left_val + right_val == target:
                break
            elif left_val + right_val > target:
                r -= 1
            else:
                l += 1
        
        result = []
        for index, val in enumerate(nums):
            if val == left_val or val == right_val:
                result.append(index)
        return result
