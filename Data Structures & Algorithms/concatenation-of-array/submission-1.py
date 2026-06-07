class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat_arr = nums * 2
        return concat_arr

sol = Solution()
nums = [1,4,1,2]
sol.getConcatenation(nums)