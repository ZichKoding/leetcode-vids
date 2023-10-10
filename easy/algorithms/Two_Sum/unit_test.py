import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
        
    def test_two_sum(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.sol.twoSum(nums, target), [0, 1])
        
    def test_two_sum_2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.sol.twoSum(nums, target), [1, 2])
        
    def test_two_sum_3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.sol.twoSum(nums, target), [0, 1])
        
    def test_two_sum_nums_len_small_constraint(self):
        nums = [3]
        target = 6
        val_err = "The length of nums is not within the constraint of 2 <= nums.length <= 103."
        with self.assertRaises(ValueError) as context:
            self.sol.twoSum(nums, target)
            self.assertEqual(val_err, context.exception.args[0])
    
    def test_two_sum_nums_len_large_constraint(self):
        nums = [0] * 105
        target = 6
        val_err = "The length of nums is not within the constraint of 2 <= nums.length <= 103."
        with self.assertRaises(ValueError) as context:
            self.sol.twoSum(nums, target)
            self.assertEqual(val_err, context.exception.args[0])
        
    def test_two_sum_nums_integer_size_constraint(self):
        nums = [-110, 0, 110]
        target = 6
        self.assertEqual(self.sol.twoSum(nums, target), None)
        
    def test_two_sum_target_integer_large_constraint(self):
        nums = [3, 2, 4]
        target = 110
        self.assertEqual(self.sol.twoSum(nums, target), None)
        
    def test_two_sum_target_integer_small_constraint(self):
        nums = [3, 2, 4]
        target = -110
        self.assertEqual(self.sol.twoSum(nums, target), None)
        