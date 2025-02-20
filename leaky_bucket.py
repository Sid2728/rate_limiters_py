import time
from collections import deque

class LeakyBucket:
    def __init__(self,capacity,leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.bucket = deque()
        self.last_leak = time.time()
    

    def allow_requests(self):
        now = time.time()
        leaked_tokens = int((now - self.last_leak)*self.leak_rate)

        if leaked_tokens>0:
            for _ in range(min(len(self.bucket),leaked_tokens)):
                self.bucket.popleft()
            self.last_leak = now
        
        if len(self.bucket)<self.capacity:
            self.bucket.append(now)
            return True
        return False

limiter = LeakyBucket(capacity=5, leak_rate=1)

for _ in range(10):
    print(limiter.allow_requests())
    time.sleep(0.1)
