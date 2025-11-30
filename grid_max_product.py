# given a 20x20 matrix of numbers, find the max product of 4 adjacent numbers in the same direction (up, down, left,
# right, diagonally)

# input processing
grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)


# brute force
def brute_force(matrix):
    # I think we can get this done in O(n^2) with a bunch of extra steps
    # though I wonder if there's some linear algebra optimization as a tribute to Euler
    size = 20
    max_product = 0
    row = 0
    col = 0
    while row < size:
        while col < size:
            current = matrix[row][col]
            # check same row
            if col < size - 3:
                # need 3 more columns on the right
                r_next1 = matrix[row][col+1]
                r_next2 = matrix[row][col+2]
                r_next3 = matrix[row][col+3]
                same_row_product = current * r_next1 * r_next2 * r_next3
                if same_row_product > max_product:
                    max_product = same_row_product
            # check same column
            if row < size - 3:
                # need 3 more rows on the right
                c_next1 = matrix[row+1][col]
                c_next2 = matrix[row+2][col]
                c_next3 = matrix[row+3][col]
                same_col_product = current * c_next1 * c_next2 * c_next3
                if same_col_product > max_product:
                    max_product = same_col_product
            # check diagonal right
            if col < size - 3 and row < size - 3:
                # there are enough rows & columns left on the right
                d_next1 = matrix[row+1][col+1]
                d_next2 = matrix[row+2][col+2]
                d_next3 = matrix[row+3][col+3]
                same_d_product = current * d_next1 * d_next2 * d_next3
                if same_d_product > max_product:
                    max_product = same_d_product
            # check diagonal left
            if col > 2 and row < size - 3:
                # need space to go left (hai hai)
                # need 3 rows on the bottom to extend to (hai hai)
                dl_next1 = matrix[row+1][col-1]
                dl_next2 = matrix[row+2][col-2]
                dl_next3 = matrix[row+3][col-3]
                same_dl_product = current * dl_next1 * dl_next2 * dl_next3
                if same_dl_product > max_product:
                    max_product = same_dl_product
            # move on
            col += 1
        row += 1
    return max_product


print(brute_force(grid))
