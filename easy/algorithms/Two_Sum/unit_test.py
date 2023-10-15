import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
        
        self.vars = {
            "two_sum_1": {
                "nums": [2, 7, 11, 15],
                "target": 9,
                "answer": [0, 1]
            },
            "two_sum_2": {
                "nums": [3, 2, 4],
                "target": 6,
                "answer": [1, 2]
            },
            "two_sum_3": {
                "nums": [3, 3],
                "target": 6,
                "answer": [0, 1]
            },
            "two_sum_nums_len_small_constraint": {
                "nums": [3],
                "target": 6,
                "answer": "The length of nums is not within the constraint of 2 <= nums.length <= 104."
            },
            "two_sum_nums_len_large_constraint": {
                "nums": [0] * 105,
                "target": 6,
                "answer": "The length of nums is not within the constraint of 2 <= nums.length <= 104."
            },
            "two_sum_nums_integer_size_constraint": {
                "nums": [-110, 0, 110],
                "target": 6,
                "answer": None
            },
            "two_sum_target_integer_large_constraint": {
                "nums": [3, 2, 4],
                "target": 110,
                "answer": "The target is not within the constraint of -109 <= target <= 109."
            },
            "two_sum_target_integer_small_constraint": {
                "nums": [3, 2, 4],
                "target": -110,
                "answer": "The target is not within the constraint of -109 <= target <= 109."
            }
        }
        
    def test_two_sum(self):
        """
            This is a test for the twoSum function. It's goal is to make sure that the function is working properly
            on a known input and a known output of the indices. 
        """
        ts = self.vars['two_sum_1']
        nums = ts['nums']
        target = ts['target']
        answer = ts['answer']
        self.assertEqual(self.sol.twoSum(nums, target), answer)
        
    def test_two_sum_2(self):
        """
            This is a test for the twoSum function. It's goal is to make sure that the function is working properly
            on a known input and a known output of the indices. 
        """
        ts = self.vars['two_sum_2']
        nums = ts['nums']
        target = ts['target']
        answer = ts['answer']
        self.assertEqual(self.sol.twoSum(nums, target), answer)
        
    def test_two_sum_3(self):
        """
            This is a test for the twoSum function. It's goal is to make sure that the function is working properly
            on a known input and a known output of the indices. 
        """
        ts = self.vars['two_sum_3']
        nums = ts['nums']
        target = ts['target']
        answer = ts['answer']
        self.assertEqual(self.sol.twoSum(nums, target), answer)
        
    def test_two_sum_nums_len_small_constraint(self):
        """
            This is a test for the twoSum function. It's goal is to make sure that 
            the function is working properly with the length of the list being too small. 
        """
        ts = self.vars['two_sum_nums_len_small_constraint']
        nums = ts['nums']
        target = ts['target']
        val_err = ts['answer']
        with self.assertRaises(ValueError) as context:
            self.sol.twoSum(nums, target)
            self.assertEqual(val_err, context.exception.args[0])
    
    def test_two_sum_nums_len_large_constraint(self):
        """ 
            This is a test for the twoSum function. It's goal is to make sure that
            the function is working properly with the length of the list being too large. 
        """
        ts = self.vars['two_sum_nums_len_large_constraint']
        nums = ts['nums']
        target = ts['target']
        val_err = ts['answer']
        with self.assertRaises(ValueError) as context:
            self.sol.twoSum(nums, target)
            self.assertEqual(val_err, context.exception.args[0])
        
    def test_two_sum_nums_integer_size_constraint(self):
        """
            This is a test for the twoSum function. It's goal is to make sure that the 
            function is working properly with returning none when the list does not 
            contain the answer for the target and the numbers in the list are too small 
            or too large.
        """
        ts = self.vars['two_sum_nums_integer_size_constraint']
        nums = ts['nums']
        target = ts['target']
        answer =ts['answer']
        self.assertEqual(self.sol.twoSum(nums, target), answer)
        
    def test_two_sum_target_integer_large_constraint(self):
        """
            This is a test for the twoSum function. It's goal is to make sure that the 
            function is working properly with raising an error when the target value 
            is too large. 
        """
        ts = self.vars['two_sum_target_integer_large_constraint']
        nums = ts['nums']
        target = ts['target']
        val_err = ts['answer']
        with self.assertRaises(ValueError) as context:
            self.sol.twoSum(nums, target)
            self.assertEqual(val_err, context.exception.args[0])
        
    def test_two_sum_target_integer_small_constraint(self):
        """
            This is a test for the twoSum function. It's goal is to make sure that the 
            function is working properly with raising an error when the target value 
            is too small. 
        """
        ts = self.vars['two_sum_target_integer_large_constraint']
        nums = ts['nums']
        target = ts['target']
        val_err =ts['answer']
        with self.assertRaises(ValueError) as context:
            self.sol.twoSum(nums, target)
            self.assertEqual(val_err, context.exception.args[0])
        