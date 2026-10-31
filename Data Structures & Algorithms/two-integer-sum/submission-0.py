class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = 0
        r = len(nums)-1

        while l<r:
            left_val, right_val = nums[l], nums[r]
            if left_val + right_val == target:
                return [l,r]
            elif left_val + right_val > target:
                r -= 1
            else:
                l += 1