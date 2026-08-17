class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            s = str(x)[::-1]
        else:
            s = str(-x)[::-1]
            s = '-' + s
        val = int(s)
        if  -2147483648 <= val <= 2147483647:
            return val
        else:
            return 0
         
        