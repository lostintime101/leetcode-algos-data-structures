from typing import List

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in range(len(strs)-1):
            ret += (strs[i] + ":;")
        ret += (strs[-1])
        return ret

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str: str) -> List[str]:

        ciphertext = str
        ans = []
        curr = ciphertext[0]
        for i in range(1, len(ciphertext)):
            if (ciphertext[i] == ":") and (ciphertext[i+1] == ";"):
                ans.append(curr)
                curr = ""
            elif ciphertext[i] == ";" and (ciphertext[i-1] == ":"): continue
            else: curr += ciphertext[i]
        ans.append(curr)
        return ans


solution = Solution()

test1 =["leet","code","love","you"]
encoded = solution.encode(test1)
print("encoded", encoded)
answer = solution.decode(encoded)
print("answer:", answer)
print(test1 == answer)

test2 = ["we", "say", ":", "yes"]
encoded = solution.encode(test2)
print("encoded", encoded)
answer = solution.decode(encoded)
print("answer:", answer)
print(test2 == answer)

