from collections import deque

def flood_fill(matrix, start_row, start_col, replacement_color):
    target_color = matrix[start_row][start_col]
    if target_color == replacement_color:
        return matrix  

    rows, cols = len(matrix), len(matrix[0])
    queue = deque()
    queue.append((start_row, start_col))

    while queue:
        r, c = queue.popleft()
        if matrix[r][c] != target_color:
            continue
        matrix[r][c] = replacement_color

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols and matrix[new_r][new_c] == target_color:
                queue.append((new_r, new_c))

    return matrix

with open("input.txt", "r") as f:
    size_line = f.readline().strip()
    start_line = f.readline().strip()
    replacement_color = f.readline().strip().strip("'").strip('"')

    height, width = map(int, size_line.split(','))
    start_row, start_col = map(int, start_line.split(','))

    matrix = []
    for _ in range(height):
        row = f.readline().strip()
        row = row.replace('[', '').replace(']', '').replace("'", '').replace('"', '')
        matrix.append([cell.strip() for cell in row.split(',')])

result = flood_fill(matrix, start_row, start_col, replacement_color)

with open("output.txt", "w") as f:
    for row in result:
        formatted_row = '[' + ', '.join(f"'{cell}'" for cell in row) + ']'
        f.write(formatted_row + '\n')