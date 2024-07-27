from typing import List


class Solution:
    # Binary search algorithem solutijon
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    """
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(isSerachLeft: bool):
            left = 0
            right = len(nums) - 1
            res = -1

            while left <= right:
                mid = (right + left) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    res = mid
                    if isSerachLeft:
                        right = mid - 1
                    else:
                        left = mid + 1

            return res

        left = search(True)
        right = search(False)

        return [left, right]


solution = Solution()
# nums = [4, 5, 6, 7, 0, 1, 2]
# index = solution.search(sorted(nums), 0)

range = solution.searchRange([2, 2], 2)
print(range)


# print(nums[index])  # 4
