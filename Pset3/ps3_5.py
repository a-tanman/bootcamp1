from copy import deepcopy

def transpose_matrix(mat):

    new_mat = deepcopy(mat)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            new_mat[j][i] = mat[i][j]

    print(new_mat)

transpose_matrix([[1,2,3],[4,5,6],[7,8,9]])
