
from collections import deque

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
    [5,0,1,0,1],
    [2,0,1,4,1],
    [1,1,0,1,0],
    [33,1,0,0,2],
]


visited = [0 for i in range(len(matrix))]
for i in range(len(visited)):
    visited[i] = [0 for j in range(len(matrix[0]))]

#print(f"number of islands is {count_islands(matrix)}")

def depth_first_search(i, j , matrix):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]):
        return

    if visited[i][j] == 1:
        return

    print(matrix[i][j])
    visited[i][j] = 1
    depth_first_search(i - 1, j, matrix)
    depth_first_search(i, j - 1, matrix)
    depth_first_search(i + 1, j, matrix)
    depth_first_search(i, j + 1, matrix)

    pass

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         depth_first_search(i, j , matrix)

def breadth_first_search(matrix):

    visited = [False for i in range(len(matrix))]
    for i in range(len(visited)):
        visited[i] = [False for j in range(len(matrix[0]))]

    q = deque()

    q.append([0, 0])

    while q:
        value = q.pop()

        i = value[0]
        j = value[1]
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or visited[i][j]:
            continue

        print(matrix[i][j])
        visited[i][j] = True
        q.append([i, j - 1])
        q.append([i, j + 1])
        q.append([i - 1, j])
        q.append([i + 1, j])


breadth_first_search(matrix)