"""
Hello#World
5#Hello5#World
12#HelloHellohi5#World
ij             i
               j
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        outputs = []
        while j < len(s):
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            outputs.append(word)
            i = j+1+length
            j = i
        
        return outputs
        
