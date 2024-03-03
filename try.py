import os
#file_path = os.path.abspath(__file__)
#file_path=os.getcwd()
#print(file_path)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Get the first row
def get_row(matrix, row_index):
    return matrix[row_index]

# Get the first column
def get_column(matrix, column_index):
    return [row[column_index] for row in matrix]

# Example usage
#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Number of rows
#num_rows = len(matrix)

# Number of columns (assuming at least one row exists)
#num_columns = len(matrix[0]) if matrix else 0

#print(f"Number of rows: {num_rows}")
#print(f"Number of columns: {num_columns}")
Total_calories = [1.1, 1.2, 1.3, 1.4, 1.5, 1]
Total_calories.clear()
print(Total_calories)