class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed
        cars = list(zip(position, speed))

        # Sort cars from closest to target to farthest
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:
            # Time needed for this car to reach the target
            time = (target - pos) / spd

            stack.append(time)

            # Car joins fleet ahead if it catches up
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


'''
Logic:
pair each car's position with its speed

sort cars by position in descending order
(start with the car closest to the target)

for each car:
calculate how long it takes to reach the target

if this car reaches the target faster than or at the same time
as the fleet directly ahead of it, it will catch up and join that fleet

otherwise, it forms a new fleet

the number of fleets is the number of times stored in the stack

Pattern:
Monotonic Stack

Time Complexity:
O(n log n)
sorting the cars takes O(n log n)
the stack operations take O(n)

Space Complexity:
O(n)
the stack can store up to n fleet arrival times

Time to complete problem:
~35 minutes
'''