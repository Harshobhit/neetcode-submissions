class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        curr_prod = 1

        zero_count = nums.count(0)

        if zero_count > 1: #All products zero
            result = [0] * len(nums)

        elif zero_count == 1:
            total_prod_without_zero = math.prod(x for x in nums if x != 0)
            result = [0 if num!=0 else total_prod_without_zero for num in nums]

        else: 
            total_prod = math.prod(nums)
            result = [total_prod//num for num in nums]
        return result