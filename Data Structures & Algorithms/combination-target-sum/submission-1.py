class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(curr_index, curr_arr):
            curr_sum = sum(curr_arr)
            if curr_sum == target:
                result.append(curr_arr.copy())
                return
            if curr_sum > target:
                return
            
            for index in range(curr_index, len(nums)):
                curr_arr.append(nums[index])
                dfs(index, curr_arr)
                curr_arr.pop()
        
        dfs(0, [])
        return result