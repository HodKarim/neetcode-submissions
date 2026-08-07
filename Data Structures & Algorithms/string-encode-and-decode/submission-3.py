class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return "".join(res)

    def decode(self, strs: str) -> List[str]:
        final_list = []
        i = 0
        while i < len(strs):
            j = i
            while strs[j] != '#':
                j += 1
            length = int(strs[i:j])
            word = strs[j + 1 : j + 1 + length]
            final_list.append(word)
            i = j + 1 + length
        return final_list