# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf = collections.deque()
        
    def read(self, buf: List[str], n: int) -> int:
        cur = 0
        cache = [''] * 4
        while cur < n:
            cnt = read4(cache)
            if not cnt:
                break
            tmpcur = min(n - cur, cnt)
            self.buf.extend(cache[:cnt])
            
            cur += tmpcur
        return cur
        
        