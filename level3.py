def fill_matrix_with_desks(m, n, num_desks):
    # Initialize the m x n matrix with zeros
    matrix = [[0] * n for _ in range(m)]
    
    desk_id = 1  # Start desk IDs from 1
    desk_count = 0  # Track the number of placed desks

    # Place desks in a structured manner
    for i in range(m):
        for j in range(n):
            # Check for horizontal placement (1x3) within bounds and empty cells
            if desk_count < num_desks and j + 2 < n and matrix[i][j] == 0 and matrix[i][j + 1] == 0 and matrix[i][j + 2] == 0:
                # Place a 1x3 desk horizontally
                matrix[i][j] = matrix[i][j + 1] = matrix[i][j + 2] = desk_id
                desk_id += 1
                desk_count += 1
                j += 2  # Move to the next position after the desk

            # Check for vertical placement (3x1) if horizontal is not possible
            elif desk_count < num_desks and i + 2 < m and matrix[i][j] == 0 and matrix[i + 1][j] == 0 and matrix[i + 2][j] == 0:
                # Place a 3x1 desk vertically
                matrix[i][j] = matrix[i + 1][j] = matrix[i + 2][j] = desk_id
                desk_id += 1
                desk_count += 1

            # Stop placing desks if we've placed the required number
            if desk_count >= num_desks:
                break
        if desk_count >= num_desks:
            break

    return matrix

def read_input(filename):
    configurations = []
    with open(filename, 'r') as file:
        # Read the number of configurations from the first line
        num_cases = int(file.readline().strip())
        
        for _ in range(num_cases):
            line = file.readline().strip()
            if line:  # Only process non-empty lines
                try:
                    cols, rows, counter = map(int, line.split())
                    configurations.append((rows, cols, counter))  # Store as (m, n, num_desks)
                except ValueError:
                    print(f"Skipping invalid line: '{line}'")
    return configurations

def write_output(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(" ".join(map(str, row)) + "\n")

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
    with open(output_file, 'w') as file:
        for matrix in all_matrices:
            for row in matrix:
                file.write(" ".join(map(str, row)) + "\n")
            file.write("\n")  # Blank line between matrices

if __name__ == "__main__":
    main()
