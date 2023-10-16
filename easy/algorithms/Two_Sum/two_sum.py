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
        # Check the length of nums is within the constraint.
        if len(nums) < 2 or len(nums) > 104:
            raise ValueError("The length of nums is not within the constraint of 2 <= nums.length <= 103.")
        
        # Check if the target is within the constraint.
        if target < -109 or target > 109:
            raise ValueError("The target is not within the constraint of -109 <= target <= 109.")
        
        # Add a hash table dictionary
        hash_table = {}

        # For loop to iterate through the list of numbers.
        for i, num in enumerate(nums):
            # Check if the number is within the constraint.
            if num < -109 or num > 109:
                print("The number is not within the constraint of -109 <= nums[i] <= 109.")
                continue
            # if length of hash table is 0, 
            # then add to the hash table and 
            # continue to next iteration. 
            if len(hash_table) == 0:
                hash_table[num] = i
                continue

            check = target - num

            if check in hash_table:
                return [hash_table[check], i]
            else:
                hash_table[num] = i
        
        return None