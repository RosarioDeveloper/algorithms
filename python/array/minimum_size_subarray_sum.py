from typing import List

"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left = 0
    curr = 0
    ans = []

    for right in range(len(nums)):
        curr += nums[right]

        while curr >= target:
            ans.append(right - left + 1)
            curr -= nums[left]
            left += 1

    if not ans:
        return 0

    return min(ans)
