class TimeMap:

    """
    Strategy: here we are essentially just storing kv pairs with values in a 
    list alongside their timestamp. When someone calls get() on a key w timestamp,
    we binary search that list if it exists to find val w greatest timestamp_prev <= timestamp.
    """

    def __init__(self):
        self.entries = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.entries:
            self.entries[key] = [(value, timestamp)]
        else:
            self.entries[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.entries:
            return ""
        
        vals = self.entries[key]

        l, r = 0, len(vals)-1
        res = ""

        while (l <= r):
            m = (l+r) // 2
            if vals[m][1] <= timestamp:
                res = vals[m][0]
                l = m + 1
            else:
                r = m - 1

        
        return res

        
