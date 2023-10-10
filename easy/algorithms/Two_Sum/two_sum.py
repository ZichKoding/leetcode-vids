from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            This function finds the indices of two numbers that add up to the target and 
            returns them in a list. Only one valid answer will be returned. 
            
            Constraints:
                * 2 <= nums.length <= 104
                * -109 <= nums[i] <= 109
                * -109 <= target <= 109
                * Only one valid answer returns. 
            
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        answer = None
        
        # Check the length of nums is within the constraint.
        if len(nums) < 2 or len(nums) > 104:
            raise ValueError("The length of nums is not within the constraint of 2 <= nums.length <= 103.")
        
        # For loop to iterate through the list of numbers.
        for i, num in enumerate(nums):
            # Check if the number is within the constraint.
            if num < -109 or num > 109:
                print("The number is not within the constraint of -109 <= nums[i] <= 109.")
                continue
            
            # Check if the target is within the constraint.
            if target < -109 or target > 109:
                print("The target is not within the constraint of -109 <= target <= 109.")
                continue
            
            # For loop to iterate through the list of numbers.
            for j, num2 in enumerate(nums):
                # Check if the number is within the constraint.
                if num < -109 or num > 109:
                    print("The number is not within the constraint of -109 <= nums[i] <= 109.")
                    continue
                
                # Check if the sum of the two numbers is equal to the target.
                if num + num2 == target:
                    # Check if the indices are not the same.
                    if i != j:
                        answer = [i, j]
                        break
            # Check if the answer is not None.
            if answer is not None:
                break
        
        return answer