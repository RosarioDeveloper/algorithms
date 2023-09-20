from typing import List
import math


#REVERSE STRING
class ArrayAlgorithms:
   def reverseString(self, s: List[str]) -> None:
      """
      PROBLEM: String Reverse
      Write a function that reverses a string. The input string is given as an array of characters 
      """
      left = 0
      right = len(s) -1
      arr= []
        
      while left <= right:
         index = right - left
         arr.append(s[index])
         left += 1

      s[:] = arr
      print(s)

   def sortedSquares(self, nums: List[int]) -> List[int]:
      nums.sort(key=abs)
      nums = list(map(lambda num : int(math.pow(abs(num), 2)) , nums))

      print(nums)
      return nums
      


arrays = ArrayAlgorithms()
# arrays.reverseString(['h','e','l','l','o'])
arrays.sortedSquares([-7,-3,2,3,11])

