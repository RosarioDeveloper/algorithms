from collections import defaultdict
from typing import List


def maximumSubarraySum(nums: List[int], k: int) -> int:
    ans = [0]
    if k <= 0:
        return 0

    for i in range(len(nums)):
        count = 0
        left = i
        counter: defaultdict = defaultdict(int)
        rows = []

        while count < k:
            count += 1
            if left > (len(nums) - 1):
                continue

            counter[nums[left]] += 1
            if counter.get(nums[left]) > 1:
                rows = []
            else:
                rows.append(nums[left])

            left += 1

        if len(rows) >= k :
            ans.append(sum(rows))

    return min(ans) 


res = maximumSubarraySum([2, 3, 1, 2, 4, 3], 7)
print(res)
