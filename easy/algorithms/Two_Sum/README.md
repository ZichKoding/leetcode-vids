# [Two Sum](https://leetcode.com/problems/two-sum/description/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

### Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
### Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

#

## My Solution: 

The solution I went with was a TDD approach. I decided to write the tests for the criteria above, well, as close as i could. Once, I finished those tests, I then started coding my solution. 

### **Unit tests:**

To get started, I imported the unittest module and the class, Solution(), from my module, two_sum. I created a class, TestTwoSum, and started with the setUp method to initiate the Solution class.  

The first three tests I created were for the three examples shown in the example. 

The next tests were for the first constraint. I created a test for a list less than 2 in length to raise a ValueError with the message, "The length of nums is not within the constraint of 2 <= nums.length <= 103." The second test for the first constraint used the same message and, also, raised a ValueError, but was testing for a length longer than 104. 

The next test I tried both, -110 and 110 to test the heighest value to make sure the return statement is None. I decided to leave the return statement as None on this one because the only way I could think of doing it is was with using a for loop, and didn't know if would be a good idea to return prior to finishing the loop in this case. 

For the last constraint, I had to break it into two tests. One to test the target value being over 109, and one being less than -109 and to raise a ValueError with the message, "The target value is not within the constraints of -109 to 109." 

### **Functionality:**

To start off the twoSum function I declared a variable to be None. The first two steps I could think of were to check for some of the constraints immediately. So, I checked the parameter, nums, for being less than 2 or greater than 104 and returning a ValueError. 

The next check was for the target parameter being less than -109 or greater 109. If the target is outside of those parameters, I raise a Value Error. 

Moving onto the for loop I decided to use enumerate to loop through the list and have the index and value being tracked. I immediately check the constraint for the number being interated over in the for loop is not less than -109 and greater than 109. 

Following the constraint check, I nest a for loop of the same list. If the nested index happens to be the same index of the parent for loop, the nested for loop will continue to the next iteration. Upon, that we do the same constraint check of the num as in the parent for loop. 

Finally, the actual math. I take the number from the parent loop and add to the number of the nested loop to see if it is equal to the targt. If it is, then I set answer being equal to an array of the indexes from lowest to highest and break out of the nested for loop. 

We do one last check to see if the answer is not None, and if the answer is not None, break the for loop and return the answer. 