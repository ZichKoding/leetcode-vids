from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            This function finds the indices of two numbers that add up to the target and 
            returns them in a list. Only one valid answer will be returned. 
            
            Constraints:
                * 2 <= nums.length <= 10**4
                * -10**9 <= nums[i] <= 10**9
                * -10**9 <= target <= 10**9
                * Only one valid answer returns. 
            
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """        
        # Check the length of nums is within the constraint.
        if len(nums) < 2 or len(nums) > 10**4:
            raise ValueError("The length of nums is not within the constraint of 2 <= nums.length <= 10**3.")
        
        # Check if the target is within the constraint.
        if target < -10**9 or target > 10**9:
            raise ValueError("The target is not within the constraint of -10**9 <= target <= 10**9.")
        
        # Add a hash table dictionary
        hash_table = {}

        # For loop to iterate through the list of numbers.
        for i, num in enumerate(nums):
            # Check if the number is within the constraint.
            if num < -10**9 or num > 10**9:
                print("The number is not within the constraint of -10**9 <= nums[i] <= 10**9.")
                continue

            if len(hash_table) == 0:
                hash_table[num] = i
                continue

            # subtract the target from the num
            check = target - num
            # if the check value is in the hash table return the indices
            if check in hash_table:
                return [hash_table[check], i]
            else:
                hash_table[num] = i
        
        return None