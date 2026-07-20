class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        arraytest = sorted(nums)
        count = 1
        maxcount = 1
        for i in range(len(arraytest) - 1):
            if arraytest[i+1] == arraytest[i] + 1:
                count+=1
            elif arraytest[i+1] == arraytest[i]:
                continue
            else:
                #case where its bigger
                if count > maxcount:
                    maxcount = count
                count = 1

        return max(count, maxcount)