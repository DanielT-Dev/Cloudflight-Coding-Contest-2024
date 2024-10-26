def can_place_horizontal(matrix, row, col):
    """ Check if a horizontal desk can be placed at (row, col) """
    if col + 2 >= len(matrix[0]):  # Check if there's enough space
        return False
    # Check for surrounding cells to ensure no touching
    for i in range(-1, 2):  # Check one row above, the row, and one row below
        for j in range(-1, 4):  # Check one column to the left of col, the three columns, and one column to the right
            if 0 <= row + i < len(matrix) and 0 <= col + j < len(matrix[0]):
                if matrix[row + i][col + j] == 'X':
                    return False
    return True

def can_place_vertical(matrix, row, col):
    """ Check if a vertical desk can be placed at (row, col) """
    if row + 2 >= len(matrix):  # Check if there's enough space
        return False
    # Check for surrounding cells to ensure no touching
    for i in range(-1, 4):  # Check one row above, the three rows, and one row below
        for j in range(-1, 2):  # Check one column to the left and the column itself and one column to the right
            if 0 <= row + i < len(matrix) and 0 <= col + j < len(matrix[0]):
                if matrix[row + i][col + j] == 'X':
                    return False
    return True


def fill_matrix_with_desks(m, n, num_desks):
    """Fill the matrix with non-touching desks."""
    matrix = [['.'] * n for _ in range(m)]  # Initialize matrix with dots
    desk_count = 0  # Count how many desks have been placed

    for row in range(m):
        for col in range(n):
            # Attempt to place a horizontal desk
            if desk_count < num_desks and can_place_horizontal(matrix, row, col):
                matrix[row][col] = 'X'
                matrix[row][col + 1] = 'X'
                matrix[row][col + 2] = 'X'
                desk_count += 1
                col += 2  # Move to the next possible placement

            # Attempt to place a vertical desk
            elif desk_count < num_desks and can_place_vertical(matrix, row, col):
                matrix[row][col] = 'X'
                matrix[row + 1][col] = 'X'
                matrix[row + 2][col] = 'X'
                desk_count += 1

            # Stop if we've placed the required number of desks
            if desk_count >= num_desks:
                break
        if desk_count >= num_desks:
            break

    return matrix

def read_input(filename):
    """Read input from the specified file."""
    configurations = []
    with open(filename, 'r') as file:
        num_cases = int(file.readline().strip())  # Read number of cases
        for _ in range(num_cases):
            line = file.readline().strip()
            if line:  # Only process non-empty lines
                cols, rows, counter = map(int, line.split())
                configurations.append((rows, cols, counter))  # Store as (m, n, num_desks)
    return configurations

def write_output(matrices, filename):
    """Write the output matrices to the specified file."""
    with open(filename, 'w') as file:
        for matrix in matrices:
            for row in matrix:
                file.write(" ".join(row) + "\n")
            file.write("\n")  # Blank line between matrices

def main():
    input_file = 'input.txt'  # Input file name
    output_file = 'output.txt'  # Output file name

    # Read matrix configurations from the input file
    configurations = read_input(input_file)

    all_matrices = []  # To store all matrices for writing later

    for m, n, num_desks in configurations:
        # Fill the matrix with desks
        matrix = fill_matrix_with_desks(m, n, num_desks)
        all_matrices.append(matrix)  # Append each matrix to the list

    # Write all matrices to the output file
    write_output(all_matrices, output_file)

if __name__ == "__main__":
    main()
