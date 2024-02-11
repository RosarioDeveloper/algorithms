from typing import List
from collections import defaultdict


class Solution:
    #  A pangram is a sentence where every letter of the English alphabet appears at least once.
    #  Given a string sentence containing only lowercase English letters,
    #  return true if sentence is a pangram, or false otherwise.
    def checkIfPangram(self, sentence: str) -> bool:
        curr = set()

        for i in range(len(sentence)):
            letter = sentence[i]

            if letter.isalpha():
                curr.add(letter)

        return len(curr) == 26

    # Given an array nums containing n distinct numbers in the range [0, n],
    # return the only number in the range that is missing from the array.
    def missingNumber(self, nums: List[int]) -> int:
        curr = set(nums)

        for i in range(len(curr)):
            i += 1

            if not i in curr:
                return i

    #  Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
    #  If there are duplicates in arr, count them separately.
    def countElements(self, arr: List[int]) -> int:
        count = 0

        for x in arr:
            count = x + 1
            if x + 1 in arr:
                count += 1

        return count

    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []

        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)

    #  You are given an integer array matches where matches[i] = [winneri, loseri]
    # indicates that the player winneri defeated player loseri in a match.
    # You should only consider the players that have played at least one match.
    # The testcases will be generated such that no two matches will have the same outcome.

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counts = defaultdict(int)
        ans = [set(), set()]
        matches.sort()

        for players in matches:
            i = 1
            while i < len(players):
                ans[0].add(players[0])
                counts[players[i]] += 1
                ans[1].add(players[i])
                i += 1

        for loser in counts:
            if loser in ans[0]: ans[0].remove(loser)
            if counts[loser] > 1:
                ans[1].remove(loser)

        ans[0] = sorted(list(ans[0]))
        ans[1] = sorted(list(ans[1]))
        return ans


# print(Solution().checkIfPangram('thequickbrownfoxjumpsoverthelazydoe'))
# print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
# print(Solution().countElements([1, 1, 3, 3, 5, 5, 7, 7]))
# print(Solution().intersection([[1, 4, 2, 3], [1, 8, 3, 2, 4], [15, 4, 5, 3, 2]]))
print(Solution().findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
