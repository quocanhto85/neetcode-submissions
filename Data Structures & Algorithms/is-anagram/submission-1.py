class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {char: s.count(char) for char in s}
        dict_t = {char: t.count(char) for char in t}
        return dict_s == dict_t

sol = Solution()
s = "xx"
t = "x"
sol.isAnagram(s, t)