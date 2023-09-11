# matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2],[3,4]]

row = len(matrix)
col = len(matrix[0])
if row == col:
    print()
    count = 0
    while count <= 2*row-2:
        item = []
        for i in range(row):
            for j in range(col):
                if i + j == count:
                    item.append(matrix[i][j])
        print(item[::-1])
        count += 1
else:
    print("Your matrix is not an square matrix. The matrix must be square, otherwise it will not work!")