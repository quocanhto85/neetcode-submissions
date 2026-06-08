class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict_1 = {}
        my_dict_2 = {}

        for elem in s:
            my_dict_1[elem] = my_dict_1.get(elem, 0) + 1

        for elem in t:
            my_dict_2[elem] = my_dict_2.get(elem, 0) + 1

        print('my_dict_1: ', my_dict_1)
        print('my_dict_2: ', my_dict_2)

        return my_dict_1 == my_dict_2

sol = Solution()
s = "racecar"
t = "carrace"
sol.isAnagram(s, t)