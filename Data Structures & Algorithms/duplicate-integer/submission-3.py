class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(set(nums))

        return len(set(nums)) != len(nums)

sol = Solution()
nums = [1, 2, 3, 3]
sol.hasDuplicate(nums)