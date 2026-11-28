class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(curr_index, curr_arr, total):
            if total == target:
                result.append(curr_arr.copy())
                return
            if total > target:
                return
            
            for index in range(curr_index, len(nums)):
                if total + nums[curr_index] > target:
                    return #If say in sorted position by adding the curr_index sum is greater then why to explore other indexes.
                curr_arr.append(nums[index])
                dfs(index, curr_arr, total+nums[index])
                curr_arr.pop()
        
        dfs(0, [], 0)
        return result