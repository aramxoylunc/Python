import random

class matrix :
    def __init__ (self, n, m) :
        self._n = n
        self._m = m
        self._matrix = [[random.randint(1,9) for _ in range(m)]for _ in range(n)]
        
    def __str__ (self) :
        str0 = ''
        for i in range(self._n) :
            for j in range(self._m) :
                str0 += str(self._matrix[i][j]) + ' '
            str0 += '\n'
        return str0
        
    def __add__ (self, mat2) :
        if mat2._n != self._n or mat2._m != self._m :
            return None
        result = matrix(self._n,self._m)
        for i in range(self._n) :
            for j in range(self._m) :
                result._matrix[i][j] = mat2._matrix[i][j] + self._matrix[i][j]
        return result

obj1 = matrix(3,4)
obj2 = matrix(3,4)

print(obj1)
print(obj2)
print(obj1+obj2)

