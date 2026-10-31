class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Searching for row where target would lie

        left_p, right_p = 0, len(matrix)-1
        target_row = 0
        
        while left_p <= right_p:
            mid = left_p + (right_p-left_p)//2

            if target > matrix[mid][-1]:
                left_p = mid + 1
            elif target < matrix[mid][0]:
                right_p = mid - 1
            else:
                target_row = mid
                break
        else:
            return False

        left_p, right_p = 0, len(matrix[0]) - 1

        while left_p <= right_p:
            mid = left_p + (right_p-left_p)//2

            if matrix[target_row][mid] == target:
                return True
            
            elif matrix[target_row][mid] > target:
                right_p = mid - 1
            else:
                left_p = mid + 1
        
        return False