

def find(i, j, matrix):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
        return

    if matrix[i][j] == 1:
        return
    else:
        matrix[i][j] = 1

    find(i - 1, j, matrix)
    find(i, j - 1, matrix)
    find(i + 1, j, matrix)
    find(i, j + 1, matrix)

def print_mat(matrix):
    print("----------")
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[0])):
            line += str(matrix[i][j])
            line += " "
        print(line)
    print("----------")

def count_islands(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print_mat(matrix)

            if matrix[i][j] == 0:
                count += 1
            find(i, j, matrix)
    return count

matrix = [
    [0,0,1,0,1],
    [0,0,1,0,1],
    [1,1,0,1,0],
    [1,1,0,0,0],
]

print(f"number of islands is {count_islands(matrix)}")