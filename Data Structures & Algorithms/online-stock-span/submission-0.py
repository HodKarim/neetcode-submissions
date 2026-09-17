class StockSpanner:

    def __init__(self):
        self.stock_span = []

    def next(self, price: int) -> int:
        self.stock_span.append(price)
        if len(self.stock_span) == 1:
            return 1
        
        count = 0
        stack = []
        for i in range(len(self.stock_span)-1,-1,-1):
            if self.stock_span[i] <= price:
                count+=1
            else:
                break
        return count
       



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


'''
design alg that collects daily prices for some stock and returns span of that stocks price for the current day

span in one day is max # of consec days where stock price is <= price of that day

stockspanner initialized obj of that class

so it starts with a stack essentially

int next gives span of stock price given that todays price is price


[100,80]

while 
'''