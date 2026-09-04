class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmapp = {}
        for i in range(len(position)):
            hashmapp[position[i]] = speed[i]

        mon_stack = [] # monotonic stack holding fleet arrival times
        count = 0

        position.sort(reverse=True) # o(nlogn)

        for i in range(len(position)):
            secs = (target - position[i])/hashmapp[position[i]]

            if not mon_stack or secs > mon_stack[-1]:
                count += 1
                mon_stack.append(secs)
        return count