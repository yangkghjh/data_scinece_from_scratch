#encoding:utf-8
# 获取矩阵大小
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

# 获取矩阵一行
def get_row(A, i):
    return A[i]

# 获取矩阵一列
def get_column(A, j):
    return [A_i[j]
        for A_i in A]

# 通过一个生成函数来产生一个矩阵
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i,j)
        for j in range(num_cols)]
        for i in range(num_rows)]


# ----------------------------------------------------------------
# 生成一个 5*5 矩阵，对角线唯 1，其他为 0
def is_diagonal(i, j):
    return i if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)
print identity_matrix