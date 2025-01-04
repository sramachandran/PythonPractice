class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, v in enumerate(nums):
            diff = target-v
            if diff in hash_map:
                return [hash_map[diff],i]
            else:
                hash_map[v]=i
def call_two_sum():
    solution = Solution()
    result = solution.twoSum([2,3,4,5],8)
    print(result)

call_two_sum()
"""
explanation: array of ints - nums and integer - target 
need indices of 2 numbers that amke up the target
input has 1 solution - answer should be 1 set
same element not to be used twice
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Algo: [2,7,11,15] - have the difference and 1 of the elements to find another element " 9 - each element in the list
and for the supplement and complement find the indices
 create a hash map and add each supplement with indice 
return the indice of the supllement from list and compelment from map

"""
