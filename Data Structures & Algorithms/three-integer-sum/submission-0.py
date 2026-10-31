class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, num in enumerate(nums):
            #We are fixing index i , so if that itself > 0 then no combo can be there where triplet sum is 0
            if num > 0:
                break
            
            if index > 0 and num == nums[index-1]: #For skipping duplicate 
                continue
            
            l, r = index + 1, len(nums) - 1

            #For second last index (l==r) and for last index (l>r) so won't go into loop    
            while l < r:
                three_sum = num + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    #When fixing for current index , we also need to make sure we don't count in duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return result


