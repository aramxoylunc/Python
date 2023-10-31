import random

class matrix :
    def __init__ (self, n, m) :
        self._n = n
        self._m = m
        self._matrix = [[random.randint(1,10) for _ in range(m)]for _ in range(n)]
        
    def __str__ (self) :
        str0 = ''
        for i in range(self._n) :
            for j in range(self._m) :
                str0 += str(self._matrix[i][j]) + ' '
            str0 += '\n'
        return str0

    def mean (self) :
        sum = 0
        for i in range(self._n) :
            for j in range(self._m) :
                sum += self._matrix[i][j]
        return int(sum/self._n/self._m)
    
    def sum_row (self, n) :
        sum = 0
        if n >= 0 and n < self._n :
            for i in range(self._m) :
                sum += self._matrix[n][i]
        return sum
    
    def average_column (self, m) :
        sum = 0
        if m >= 0 and m < self._m :
            for i in range(self._n) :
                sum += self._matrix[i][m]
        return sum/self._n
    
    def submatrix (self, col1, col2, row1, row2) :
        if 0 <= col1 < col2 < self._m and 0 <= row1 < row2 < self._n :
            submatrix = [[0 for _ in range(1 + col2 - col1)]for _ in range(1 + row2 - row1)]
            for i in range(row1,row2+1) :
                for j in range(col1,col2+1) :
                    submatrix[i - row1][j - col1] = self._matrix[i][j]
            return submatrix
        else :
            return None

obj = matrix(3,4)

print(obj)
print(obj.mean())
print(obj.sum_row(0))
print(obj.average_column(0))
print(obj.submatrix(0,1,0,1))


