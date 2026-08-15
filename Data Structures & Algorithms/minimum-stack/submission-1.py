class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] #we store from biggest to smallest?
        

    def push(self, val: int) -> None:
        #everytime we ADD a value we compare it to the top of the min stack
        self.stack.append(val) #add value to the regular stack

        if len(self.stack) == 1: #f thats the only elem added
            self.minstack.append(val) #add that shi to the minstack
        else:
            top = self.minstack[-1] #get the most recent from minstack
            self.minstack.append(min(top, val)) #add whatevers smaller, that elem or the recent one
        
        

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        '''
        verytime we add an element we compare it to the minimum value already in.
        '''
        return self.minstack[-1]