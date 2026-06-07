class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)

        return len(nums) != len(my_set)

sol = Solution()
nums = [1, 2, 3, 4]
sol.hasDuplicate(nums)