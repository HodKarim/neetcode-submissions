class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boat = 0
        i=0
        j=len(people)-1

        while i<=j:
            if people[j] + people[i] <= limit and i!=j:
                boat+=1
                i+=1
                j-=1
            elif people[j] + people[i] > limit and i!=j:
                j-=1
                boat+=1
            else:
                boat+=1
                i+=1
                j-=1
            
        return boat

'''
[1,2,2,3,3]
   i
   j

boat=3
'''