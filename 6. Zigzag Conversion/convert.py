class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if n == 1 or numRows == 1 or numRows == n:
            return s

        mat = [[] for _ in range(numRows)]
        row = pos = 0

        while pos < n:
            if row == 0:
                for i in range(numRows):
                    if pos >= n:
                        break
                    mat[i].append(s[pos])
                    pos += 1
                row = numRows - 2
            else:
                while row != 0 and pos < n:
                    mat[row].append(s[pos])
                    row -= 1
                    pos += 1

        result = ""
        for i in range(numRows):
            result += "".join(mat[i])
        return result