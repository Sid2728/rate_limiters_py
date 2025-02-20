import time
class TokenBucket: 
    def __init__(self,capacity,fill_rate):
        self.capacity = capacity
        self.fill_rate= fill_rate
        self.tokens= capacity
        self.last_update= time.time()
    
    def allow_requests(self, tokens=1):
        now = time.time()
        time_passed = now - self.last_update
        self.tokens = min(self.capacity, self.tokens + time_passed*self.fill_rate)
        self.last_update= now

        if self.tokens>=tokens:
            self.tokens-=tokens
            return True
        return False

limiter = TokenBucket(capacity=10,fill_rate=1)
for _ in range(11):
    print(limiter.allow_requests())
    time.sleep(0.1)
