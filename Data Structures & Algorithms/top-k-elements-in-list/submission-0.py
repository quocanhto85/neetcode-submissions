from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print('count: ', count)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        print(buckets)
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            print('buckets[freq]: ', buckets[freq])
            for num in buckets[freq]:
                result.append(num)
                print('result: ', result)
                if len(result) == k:
                    return result

nums = [1,2,2,3,3,3]
k = 2
sol = Solution()
sol.topKFrequent(nums, k)