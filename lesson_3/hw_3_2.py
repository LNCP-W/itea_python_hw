#Задание тестирует етот класс. Тест в папке 'tests' под названием 'testmatrix'
class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __add__(self, other):
        s = []
        for i in range((len(self.mat))):
            s.append([])
            for a in range(len(self.mat[i])):
                s[i].append(self.mat[i][a] + other.mat[i][a])
        return Matrix(s)

    def __sub__(self, other):
        s = []
        for i in range((len(self.mat))):
            s.append([])
            for a in range(len(self.mat[i])):
                s[i].append(int(self.mat[i][a]) - int(other.mat[i][a]))
        return Matrix(s)

    def __mul__(self, other):
        s = []
        for i in range((len(self.mat))):
            s.append([])
            for a in range(len(self.mat[i])):
                s[i].append(int(self.mat[i][a]) * other)
        return Matrix(s)

    def __truediv__(self, other):
        s = []
        for i in range((len(self.mat))):
            s.append([])
            for a in range(len(self.mat[i])):
                s[i].append((self.mat[i][a]) / other)
        return Matrix(s)

    def __str__(self):
        s = ""
        for i in self.mat:
            s = f"{s}\n{i}"
        return s

m1=Matrix([[1, 2, 3], [2, 3, 4], [3, 5, 6]])
m2=Matrix([[2, 3, 4], [3, 5, 6], [1, 2, 3]])
m3=m1+m2
print (m3)
print (m2 - m1)
print (m2 * 2)
print (m2 / 2)
print(m1)
print(m1.mat)