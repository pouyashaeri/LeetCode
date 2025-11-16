from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str +=  str(len(word)) + '#' + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while(i < len(s)):
            j = i
            while(s[j] != '#'):
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
    

Sol = Solution()
# print(Sol.encode(["neet","code","love","you"]))
print(Sol.decode("4#neet4#code4#love3#you"))
