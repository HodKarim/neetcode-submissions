from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        answer = []

        counter = Counter(nums)

        num_to_exceed = len(nums) // 3

        for key, value in counter.items():
            if value > num_to_exceed:
                answer.append(key)

        return answer

'''
given integer array nums of size n

find all elems that appear more than n/3 floor times

10//3 = 3

so whats there more than 3 times?

gonna need frequency count for this. whatever value is above that amount is added to da array





'''