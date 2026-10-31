class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            
            #Array is already sorted
            if nums[r] > nums[l]:
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1