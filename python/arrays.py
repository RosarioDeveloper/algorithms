from typing import List
import math


#REVERSE STRING
class ArrayAlgorithms:
   # PROBLEM 1 - Reverse
   # Write a function that reverses a string. The input string is given as an array of characters 
   def reverseString(self, s: List[str]) -> None:
      left = 0
      right = len(s) -1
      arr= []
        
      while left <= right:
         index = right - left
         arr.append(s[index])
         left += 1

      s[:] = arr
      print(s)

   # PROBLEM 2 - Sqaure Sorted
   # Write a function that reverses a string. The input string is given as an array of characters 
   def sortedSquares(self, nums: List[int]) -> List[int]:
      nums.sort(key=abs)
      nums = list(map(lambda num : int(math.pow(abs(num), 2)) , nums))

      print(nums)
      return nums
   
   # PROBLEM 3 - Max Average of Subarrys
   # You are given an integer array nums consisting of n elements, and an integer k.
   # Find a contiguous subarray whose length is equal to k that has the maximum 
   # average value and return this value.
   def findMaxAverage(self, nums: List[int], k: int) -> float:
      left = 0
      curr = 0
      ans = 0

      for right in range(len(nums)):
         curr += nums[right]

         while curr > k:
            curr -= nums[left]
            left += 1
         
         ans = max(ans, right - left + 1)
      
      print(ans)
      return ans


arrays = ArrayAlgorithms()
# arrays.reverseString(['h','e','l','l','o'])
# arrays.sortedSquares([-7,-3,2,3,11])
arrays.findMaxAverage([1,12,-5,-6,50,3], 4)

