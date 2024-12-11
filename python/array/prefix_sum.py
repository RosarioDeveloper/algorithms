from typing import List


def calcPrefixSum(nums: List[int], queries: List[List], limt: int):
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    for x, y in queries:
        pass

    print(prefix)


def minStartValue(nums: List[int]) -> int:
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = 1
    min_sum = min(prefix)

    if min_sum < 1:
        ans = min_sum - 1

    print(prefix)
    print(abs(ans))


def maxArea(height: List[int]) -> int:

    i = 0
    j = len(height) - 1
    maxArea = 0

    while i < j:
        width = j - i
        area = width * min(height[i], height[j])
        maxArea = max(maxArea, area)

        if height[i] < height[j]:
            i += 1;
        else: 
            j -= 1;
        

    print(maxArea)


maxArea([8, 7, 2, 1])
# minStartValue([2,3,5,-5,-1])
# calcPrefixSum([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13)
