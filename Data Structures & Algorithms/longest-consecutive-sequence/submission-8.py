class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sett = set(nums)
        maxx = 0

        for num in sett:
            if (num - 1) not in sett:
                curr_num = num
                count = 1
                while (curr_num + 1) in sett:
                    curr_num += 1
                    count += 1
                maxx = max(maxx, count)
        return maxx