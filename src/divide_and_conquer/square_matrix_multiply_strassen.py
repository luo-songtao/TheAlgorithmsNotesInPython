#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com

def get_dim(matrix):
    return len(matrix), len(matrix[0])


def divide_matrix(M):
    dim_M = get_dim(M)

    r_mid = dim_M[0]//2
    c_mid = dim_M[1]//2

    M11 = []
    M12 = []
    M21 = []
    M22 = []

    i = 0
    for r in M:
        if i < r_mid:
            M11.append(r[:c_mid])
            M12.append(r[c_mid:])
        else:
            M21.append(r[:c_mid])
            M22.append(r[c_mid:])
        i += 1
    return M11, M12, M21, M22


def add_matrix(M1, M2):
    dim_A = get_dim(M1)
    M = []
    for i in range(dim_A[0]):
        M.append(
            [M1[i][j] + M2[i][j] for j in range(dim_A[1])]
        )
    return M

def sub_matrix(M1, M2):
    dim_A = get_dim(M1)
    M = []
    for i in range(dim_A[0]):
        M.append(
            [M1[i][j] - M2[i][j] for j in range(dim_A[1])]
        )
    return M

def multi_2q_2q(m1, m2):
    for i in range(2):
        _11 = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
        _12 = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
        _21 = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
        _22 = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    return [[_11, _12],[_21, _22]]


def matrix_multiply_strassen(A, B):

    dim_A = get_dim(A)
    dim_B = get_dim(B)
    if dim_A[1] != dim_B[0]:
        raise Exception("Can't multiply matrix A{} and B{}".format(dim_A, dim_B))
    elif dim_A == (2,2) and dim_B == (2,2):
        return multi_2q_2q(A, B)
    else:
        A11, A12, A21, A22 = divide_matrix(A)
        B11, B12, B21, B22 = divide_matrix(B)

        S1 = sub_matrix(B12,B22)
        S2 = add_matrix(A11,A12)
        S3 = add_matrix(A21,A22)
        S4 = sub_matrix(B21,B11)
        S5 = add_matrix(A11,A22)
        S6 = add_matrix(B11,B22)
        S7 = sub_matrix(A12,A22)
        S8 = add_matrix(B21,B22)
        S9 = sub_matrix(A11,A21)
        S10 = add_matrix(B11,B12)

        P1 = matrix_multiply_strassen(A11, S1)
        P2 = matrix_multiply_strassen(S2, B22)
        P3 = matrix_multiply_strassen(S3, B11)
        P4 = matrix_multiply_strassen(A22, S4)
        P5 = matrix_multiply_strassen(S5, S6)
        P6 = matrix_multiply_strassen(S7, S8)
        P7 = matrix_multiply_strassen(S9, S10)

        C11 = sub_matrix(add_matrix(P5, P4), sub_matrix(P2,P6))
        C12 = add_matrix(P1, P2)
        C21 = add_matrix(P3, P4)
        C22 = sub_matrix(add_matrix(P5,P1), add_matrix(P3,P7))

        C = []
        for i in range(len(C11)):
            C.append(C11[i]+C12[i])

        for i in range(len(C21)):
            C.append(C21[i]+C22[i])
        return C


if __name__ == '__main__':
    m = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

    ret = matrix_multiply_strassen(m,m)
    print(ret)

