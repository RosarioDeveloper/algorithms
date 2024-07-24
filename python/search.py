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


solution = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
index = solution.search(sorted(nums), 0)

print(nums[index])  # 4
