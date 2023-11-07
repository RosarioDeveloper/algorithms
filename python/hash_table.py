from typing import List


class Solution:

    def checkIfPangram(self, sentence: str) -> bool:
        curr = set()

        for i in range(len(sentence)):
            letter = sentence[i]

            if letter.isalpha():
                curr.add(letter)

        return len(curr) == 26

    def missingNumber(self, nums: List[int]) -> int:
        curr = set(nums)

        for i in range(len(curr)):
            i += 1

            if not i in curr:
                return i

    def countElements(self, arr: List[int]) -> int:
        count = 0

        for x in arr:
            count = x + 1
            if x + 1 in arr:
                count += 1

        return count


# print(Solution().checkIfPangram('thequickbrownfoxjumpsoverthelazydoe'))
# print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(Solution().countElements([1, 1, 3, 3, 5, 5, 7, 7]))
