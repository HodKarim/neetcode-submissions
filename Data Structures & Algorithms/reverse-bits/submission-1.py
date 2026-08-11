class Solution:
    def reverseBits(self, n: int) -> int:
        number = []
        for i in range(32):
            bit = n & 1
            number.append(str(bit))
            n = n >> 1
        answer = "".join(number)
        return int(answer, 2)