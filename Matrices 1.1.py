A = [[1, 2, 3, 4, 5], [11, 20, 30, 40, 50], [0, 1, 1, 1, 1]]
B = [[1, 5, 3, 1, 6], [1, 3, 6, 2, 4], [1, 3, 5, 6, 7], [2, 5, 7, 2, 1]]
C = [[1, 1, 1, 3], [1, 2, 3, 0], [1, 3, 4, -2]]
D = [[0, 3, 5], [5, 5, 2]]
E = [[3, 4], [3, -2], [4, -2]]
F = [[2, 2, -5], [1, 1, 20], [1, 0, 1]]
G = [[32, 5], [200, -5]]


def switch_rows(matrix, row1, row2):
    new_matrix = []
    for i in range(len(A)):
        if i == row1:
            new_matrix.append(A[row2])
        elif i == row2:
            new_matrix.append(A[row1])
        else:
            new_matrix.append(A[i])
    return new_matrix


# Adds one row to another. Operates on row2.
def add_row_to_row(matrix, row1, row2, subtraction=False):
    if subtraction is True:  # True is the switch to subtraction
        for i in range(len(matrix[0])):
            matrix[row2][i] -= matrix[row1][i]
    else:
        for i in range(len(matrix[0])):
            matrix[row2][i] += matrix[row1][i]


def create_identity_matrix(size):
    i_matrix = []
    count = 0
    for i in range(size):
        i_matrix.append([])
        for j in range(size):
            count += 1
            if count % 2 == 0:
                i_matrix[i].append(0)
            else:
                i_matrix[i].append(1)
    return i_matrix


def create_zero_matrix(rows, columns):
    z_matrix = []
    for i in range(rows):
        z_matrix.append([])
        for j in range(columns):
            z_matrix[i].append(0)
    return z_matrix


# *-1 to all contents.
def create_opposite_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for num in matrix[i]:
            new_matrix[i].append(num*-1)
    return new_matrix


# Prints it out into a non list form.
def pretty_matrix(matrix, spaces=10):
    for i in range(len(matrix)):
        first = 0
        for num in matrix[i]:
            num_extra_spaces = spaces
            new = 0
            count = 0
            while new != "ass":  # Count = digits in the number
                new = abs(num) - 10 ** (count + 1)
                if new < 0:
                    new = "ass"
                    break
                count += 1
            num_extra_spaces -= count  # Everything to line up
            if num < 0:
                num_extra_spaces -= 1   # "-" adds an extra space
            if first == 0:
                print("|" + str(num), end=" " * num_extra_spaces)
                first += 1
            else:
                print(num, end=" " * num_extra_spaces)
        print("")
    print("")


def mult_matrices(m1, m2):
    rows_1 = len(m1)
    cols_1 = len(m1[0])
    rows_2 = len(m2)
    cols_2 = len(m2[0])
    if cols_1 != rows_2:
        print("Cannot multiply a {a}x{b} with a {c}x{d} matrix".format(a=rows_1, b=cols_1, c=rows_2, d=cols_2))
        return 1
    new_matrix = []
    for row1 in range(rows_1):  # corresponds to the mathematician working left to right
        new_matrix.append([])   # each list is a new row. Adds a new row
        for col2 in range(cols_2):  # Working top to bottom
            total = 0
            for col1 in range(cols_1):  # cols_1 would be referring more so to the number's index.
                total += m1[row1][col1] * m2[col1][col2]
            new_matrix[row1].append(total)  # Total is the total from dot product
    return new_matrix


def determinant(matrix):    # Thus far, this works for 2x2
    total_formula = 0
    primo_old = 1  # This needs to be reset every primo
    input_matrix = matrix
    new_matrix = []  # This needs to be reset every primo

    even_odd = 0  # This needs to be reset every row nest (new matrix)
    primo = 1
    primo_row = 0   
    primo_col = 0
    rows = len(matrix)  # Dimensions need to be reset every row reset (new matrix) 
    cols = len(matrix[0])

    if rows != cols:
        print("Need an x by x matrix")
        return 1

    def step1(matrix2):
        row_count = 0   # for creating matrices
        if even_odd % 2 == 0:
            primo = matrix2[0][primo_col] * primo_old
        else:
            primo = matrix2[0][primo_col] * primo_old * (-1)
        for row_i in range(rows):
            if row_i <= primo_row:  # Rejects rows at or before primo_row
                continue
            new_matrix.append([])
            for col_i in range(cols):
                if col_i == primo_col:  # primo index vs column
                    continue
                new_matrix[row_count].append(matrix2[row_i][col_i])  # add num to newest row

            row_count += 1
        if len(new_matrix[0]) == 1 and len(new_matrix) == 1:
            print(new_matrix)  # DEBUG
            return new_matrix[0][0] * primo
        else:
            print(new_matrix)  # DEBUG
            return new_matrix
            
            
    while primo_col != cols:
        thing = step1(input_matrix)
        if type(thing) is int:
            total_formula += thing
        else:
            input_matrix = thing
            rows = len(thing)
            cols = len(input_matrix[0])
        primo_old = 1
        new_matrix = []
        even_odd += 1
        primo_col += 1

    return total_formula
            
                
def inverse_2x2(matrix):
    pass

pretty_matrix(B)

input("Press Enter to Exit")