class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)) + '#' + s)
        
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            print(s[i:j])
            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]
            result.append(word)

            i = j + 1 + length

        return result

strs = ["Hello","World"]

solution = Solution()
encoded_string = solution.encode(strs)
decoded_strs = solution.decode(encoded_string)