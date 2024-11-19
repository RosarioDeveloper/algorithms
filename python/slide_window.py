from typing import List

""""
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
"""
def decrypt(code: List[int], k: int) -> List[int]:
    ans = [] 
    for i in range(len(code)):
        if k == 0: return [0] * len(code)

        sum = 0
        left = i + 1
        count = 1

        if k < 0:
            left = i - abs(k)

        while count <= abs(k):
            sum += code[left % len(code)]
            left += 1
            count += 1

        ans.append(sum)
        
    return ans

res = decrypt([10, 5, 7, 7, 3, 2, 10, 3, 6, 9, 1, 6], -4)
print(res)
