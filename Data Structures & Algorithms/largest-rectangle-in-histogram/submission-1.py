class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            # process bars taller than current bar
            while stack and stack[-1][1] > height:
                index, h = stack.pop()

                area = h * (i - index)
                max_area = max(max_area, area)

                start = index

            # save earliest valid start index n height
            stack.append((start, height))

        # process bars left in stack
        for index, height in stack:
            area = height * (len(heights) - index)
            max_area = max(max_area, area)

        return max_area






'''

given: array of ints heights where heights[i] is the neight of a bar

width of each is 1

return area of largest rectangle in bars


monotonic increasing stack. so we keep looking for the largest number or equal until we find something that fucks the order.


then we store the area of it?

area = []

mon_stack = []

pop all until its increasing again?

last in first out.

[7]

see 1. no longer increasing. store 7 in possible areas

store 1

[1]

[1,7]

see 2. pop 7.

[1,2]























Logic:
use a monotonic increasing stack that stores
(start_index, height)

iterate through each bar in the histogram

if the current height is smaller than the height on top
of the stack, pop bars until the stack is increasing again

for each popped bar:
calculate the largest rectangle that can use that height
update the maximum area

keep track of the earliest index where the current height
could start expanding from

push the current height and its start index onto the stack

after processing all bars, process any remaining bars
in the stack since they can extend to the end of the histogram

return the largest area found

Pattern:
Monotonic Stack (Increasing)

Time Complexity:
O(n)
each bar is pushed onto the stack once and popped once

Space Complexity:
O(n)
the stack can store up to n bars

Time to complete problem:
1hr 23 minutes (had to consult video)


        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            # Process bars that are taller than current bar
            while stack and stack[-1][1] > height:
                index, h = stack.pop()

                area = h * (i - index)
                max_area = max(max_area, area)

                start = index

            # Store earliest valid start index and height
            stack.append((start, height))

        # Process remaining bars in stack
        for index, height in stack:
            area = height * (len(heights) - index)
            max_area = max(max_area, area)

        return max_area

'''