def cross(x, y):
    matrix = [['.'] * len(x) for _ in range(len(y))]
    for i in range(len(y)):
        for j in range(len(x)):
            if x[j] == y[i]:
                for k in range(len(x)):
                    matrix[i][k] = x[k]
                for p in range(len(y)):
                    matrix[p][j] = y[p]
                return matrix

A, B = input().split()
new = cross(A, B)

for i in range(len(B)):
    for j in range(len(A)):
        print(new[i][j], end='')
    print()