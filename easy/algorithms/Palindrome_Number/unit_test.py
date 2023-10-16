import unittest

from palindrome_number import Solution


class TestProblemList(unittest.TestCase):

	def setUp(self):
		self.sol = Solution()

		self.vars = {
			"test_true_palindrome_1": {
				"input": 121,
				"output": True
			},
			"test_false_palindrome_1": {
				"input": -121,
				"output": False
			},
			"test_false_palindrome_2": {
				"input": 10,
				"output": False
			},
			"test_input_cosntraint_samllest": {
				"input": -2**31 - 1,
				"output": "The input value does not fall within the constraints of -2^31 <= input <= 2^31 -1."
			},
			"test_input_cosntraint_largest": {
				"input": 2**31,
				"output": "The input value does not fall within the constraints of -2^31 <= input <= 2^31 -1."
			}
		}

	def test_true_palindrome_1(self):
		"""
			This is to test the function isPalindrome in problem_list.py. 
			This will take an input that reads from left to right as right 
			to left and return true. 
		"""
		pn = self.vars['test_true_palindrome_1']
		x = pn['input']
		output = pn['output']
		self.assertEqual(self.sol.isPalindrome(x), output)


	def test_false_palindrome_1(self):
		"""
			This is to test the function isPalindrome in problem_list.py. 
			This will take an input that does not read from left to right 
			as right to left and return false for negative numbers.
		"""
		pn = self.vars['test_false_palindrome_1']
		x = pn['input']
		output = pn['output']
		self.assertEqual(self.sol.isPalindrome(x), output)


	def test_false_palindrome_2(self):
		"""
			This is to test the function isPalindrome in problem_list.py. 
			This will take an input that does not read from left to right 
			as right to left and return false.
		"""
		pn = self.vars['test_false_palindrome_2']
		x = pn['input']
		output = pn['output']
		self.assertEqual(self.sol.isPalindrome(x), output)


	def test_input_cosntraint_samllest(self):
		"""
			This is to test the function isPalindrome in problem_list.py. 
			This will take an input that is too small.
		"""
		pn = self.vars['test_input_cosntraint_samllest']
		x = pn['input']
		output = pn['output']
		with self.assertRaises(ValueError, msg=output):
			self.sol.isPalindrome(x)


	def test_input_cosntraint_largest(self):
		"""
			This is to test the function isPalindrome in problem_list.py. 
			This will take an input that is too large.
		"""
		pn = self.vars['test_input_cosntraint_largest']
		x = pn['input']
		output = pn['output']
		with self.assertRaises(ValueError, msg=output) as context:
			self.sol.isPalindrome(x)