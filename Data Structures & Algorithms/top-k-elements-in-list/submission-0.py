class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create dictionary to count how many times each number appears
        # key  = number from nums
        # value = frequency of that #
        count = {}

        # count frequency of every number in nums
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # create buckets where the index represents the frequency
        # (eg: bucket[3] will store all numbers that appear 3 times)

        bucket = [[] for _ in range(len(nums) + 1)]

        # put each number into the bucket that matches its frequency
        for num, freq in count.items():
            bucket[freq].append(num)

        # list will store the final top k frequent numbers
        result = []

        # Go thru the buckets from highest frequency to lowest frequency
        # most frequent numbers are near end of bucket list
        for freq in range(len(bucket) - 1, 0, -1):
            # add every num that is with this frequency
            for num in bucket[freq]:
                result.append(num)

                # ocnce we have k numd, return answer
                if len(result) == k:
                    return result


        """
        Pattern Type: Hash Map + Bucket Sort pattern.

        only need the k most frequent elements. 1st part is counting, use a hash map. 2nd parts
        finding the largest frequencies, use bucket sort.

        Time Complexity:
        O(n), because count each number once, place each unique number into
        bucket, then scan through the bucket list once

        Space Complexity:
        O(n), because hash map for the counts and a bucket list to group numbers by frequency

        How long it took: 41 minutes

        """