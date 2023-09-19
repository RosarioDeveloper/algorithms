from ast import *

class Solution:
   def reverseString(self, s: List) -> None:
      """
      PROBLEM: String Reverse
      Write a function that reverses a string. The input string is given as an array of characters 
      """
      newArray: List = []
      left = 0
      right = len(s) - 1

      while left <= right:
         index = right - left
         newArray.append(s[index])
         left += 1

      print(newArray)

#Execute
Solution().reverseString(['h','e','l','l','o'])

