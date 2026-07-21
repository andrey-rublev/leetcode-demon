class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = "".join(f"{len(s)}#{s}" for s in strs)
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            ret.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return ret