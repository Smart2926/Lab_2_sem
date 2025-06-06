import math

def insertion_sort_columns(matrix):
    rows = 0
    while True:
        try:
            _ = matrix[rows]
            rows += 1
        except IndexError:
            break

    cols = 0
    while True:
        try:
            _ = matrix[0][cols]
            cols += 1
        except IndexError:
            break

    for col in range(cols):
        for i in range(1, rows):
            x = matrix[i][col]
            j = i
            while j > 0 and matrix[j - 1][col] < x:
                matrix[j][col] = matrix[j - 1][col]
                j -= 1

            matrix[j][col] = x  

    return matrix

def geometric_mean_below_diag(matrix):
    rows = 0
    while True:
        try:
            _ = matrix[rows]
            rows += 1
        except IndexError:
            break

    geo_means = [] 
    for i in range(1, rows):
        below_diag = []
        j = 0
        while j < i:
            try:
                below_diag.append(matrix[i][j]) 
                j += 1
            except IndexError:
                break
        if below_diag: 
            product = 1
            count = 0 
            for num in below_diag:
                product *= num
                count += 1
            if product > 0:
                geo_mean = math.pow(product, 1 / count) if count > 0 else 0
            else:
                geo_mean = 0
            geo_means.append(geo_mean)
        else:
            geo_means.append(0)
    return geo_means

def sum_of_values(values):
    total = 0
    for value in values:
        total += value
    return total

matrix = [
    [9, 24, -2, 86, -3],
    [40, 49, -4, 3, 0],
    [27, -76, 77, -1, 69],
    [71, -89, 94, -51, 50],
    [2, 96, 42, 36, -1]
]

print("Оригінальна матриця:")
for row in matrix:
    print(row)

sorted_matrix = insertion_sort_columns(matrix)

print("Відсортована матриця:")
for row in sorted_matrix:
    print(row)

geo_means = geometric_mean_below_diag(sorted_matrix)
print("Значення функції f(aij) (середнє геометричне):")
print(geo_means)

F_value = sum_of_values(geo_means)
print("Значення функції F(fi(aij)):")
print(F_value)
