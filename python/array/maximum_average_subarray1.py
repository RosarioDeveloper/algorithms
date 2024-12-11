from typing import List

"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

"""

def findMaxAverage(nums: List[int], k: int) -> float:
    left = 0
    some = 0
    ans = float('-inf')

    for right in range(len(nums)):
        some += nums[right]
        size = right - left + 1
        # ans = max(ans, some)

        while size == k:
            ans = max(ans, some)
            some -= nums[left]
            left += 1
            size = right - left + 1

    return ans / k


res = findMaxAverage([-1], 1)
print(res)
