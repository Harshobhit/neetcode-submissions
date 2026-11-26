class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(arr_index, curr_arr):
            subsets.append(curr_arr.copy())
            for index in range(arr_index, len(nums)):
                curr_arr.append(nums[index])
                dfs(index + 1, curr_arr)
                curr_arr.pop(-1)
        
        dfs(0, [])
        return subsets