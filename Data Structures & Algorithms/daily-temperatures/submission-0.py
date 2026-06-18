class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # Resolve previous colder temperatures
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            # Store current day's index
            stack.append(i)

        return result


'''
Logic:
create a result array initialized with 0s
use a stack to store indices of temperatures that have not found a warmer day yet

iterate through each temperature

while the current temperature is warmer than the temperature
at the index on top of the stack:
pop the index from the stack
calculate how many days it took to find a warmer temperature
store that value in the result array

push the current index onto the stack

any indices left in the stack never find a warmer day,
so they remain 0 in the result array

Pattern:
Monotonic Stack (Decreasing)

Time Complexity:
O(n)
each index is pushed onto the stack once and popped once

Space Complexity:
O(n)
the stack can store up to n indices in the worst case

Time to complete problem:
~25 minutes
'''