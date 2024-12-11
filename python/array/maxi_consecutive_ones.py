""""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""


from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        max_zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                max_zeros += 1

            while max_zeros > k:
                if nums[left] == 0:
                    max_zeros -= 1

                left += 1

            ans = max(ans, i - left + 1)
        
        return ans


solution = Solution()

print(solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
