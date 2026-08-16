class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        if n == 0:
            return 0

        i = 0
        neg = False

        if s[0] == '-':
            neg = True
            i += 1
        elif s[0] == '+':
            i += 1

        if i >= n or s[i].isdigit() == False:
            return 0


        inti = 0
        while i < n and s[i].isdigit():
            inti = inti * 10 + int(s[i])
            i += 1
            # early clamp to avoid growing huge numbers on long digit strings
        if neg:
            inti = -inti
        
        if inti > 2147483647:
            inti = 2147483647
        elif inti < -2147483648 :
            inti = -2147483648 
        return inti