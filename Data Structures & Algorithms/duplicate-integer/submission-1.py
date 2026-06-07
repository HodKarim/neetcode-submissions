class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create empty set to store numbers we've already seen
        # set is good because checking if something exists in it is fast
        seen = set()

        # go thru each number in  input list one by one
        for num in nums:
            # if number's already in the set, means there's duplicate
            if num in seen:
                return True

            # if number has not been seen before, add to set
            seen.add(num)

        # if finish checking every # & never find repeated value, then  list has no duplicates
        return False


        """
        Pattern Type: Hash Set pattern.

        Use a set to keep track of values.

        Time Complexity:
        O(n), because we check each number once.

        Space Complexity:
        O(n), because in the worst case, all numbers are unique and stored
        in the set.

        How long it took: 5 minutes fully, 10 to write out logic
        """