import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        print('output before left: ', output)

        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output

nums = [1,2,4,6]
sol = Solution()
sol.productExceptSelf(nums)