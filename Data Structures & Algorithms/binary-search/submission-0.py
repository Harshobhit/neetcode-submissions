class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_p, right_p = 0 , len(nums)-1

        while left_p <= right_p:
            mid = left_p + (right_p-left_p)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right_p = mid - 1
            else:
                left_p = mid + 1
        
        return -1