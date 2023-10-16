from typing import List


class Solution:
    def __init__(self):
        self.num_list = []


    def isPalindrome(self, x: int) -> bool:
        """
            This function is to return true when a number reads from right to left as let to right.
            All negative numbers will return false.

            :type x: int
            :rtype: bool
        """

        # Check if the input is too low and raise an error.
        lowest = -2**31
        highest = 2**31 - 1

        print(x)

        if lowest > x > highest:
            raise ValueError("The input value does not fall within the constraints of -2^31 <= input <= 2^31 -1.")
        
        if x < 0:
            return False

        self.individual_number_list(x)

        if self.num_list == self.num_list[::-1]:
            return True

        return False


    def individual_number_list(self, x: int) -> List[int]:
        """
            Break the number down into the individual numbers and return as a list to check
            if the item is a palindrome number.
        """

        self.num_list.append(x % 10)

        remainder = x // 10
        if remainder != 0:
            self.individual_number_list(remainder)
        else:
            return self.num_list

