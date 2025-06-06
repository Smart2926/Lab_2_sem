import math

class Matrix:
    def __init__(self, data):
        self.data = data

    def get_rows(self):
        rows = 0
        for _ in self.data:
            rows += 1
        return rows

    def get_columns(self):
        if self.data:
            columns = 0
            for _ in self.data[0]:
                columns += 1
            return columns
        return 0

    def print_matrix(self, message="Matrix:"):
        print(message)
        for row in self.data:
            print(row)

    def sort_columns_decorator(self, method):
        def wrapper(*args, **kwargs):
            rows = self.get_rows()
            columns = self.get_columns()

            for col in range(columns):
                for i in range(1, rows):
                    x = self.data[i][col]
                    j = i
                    while j > 0 and self.data[j - 1][col] < x:
                        self.data[j][col] = self.data[j - 1][col]
                        j -= 1
                    self.data[j][col] = x
            return method(*args, **kwargs)
        return wrapper

    def geometric_mean_below_diag(self):
        rows = self.get_rows()
        geo_means = []
        for i in range(rows):
            below_diag = []
            for j in range(i):
                below_diag.append(self.data[i][j])
            product = 1
            count = 0
            for num in below_diag:
                product *= num
                count += 1
            if count > 0 and product > 0:
                geo_mean = math.pow(product, 1 / count)
                geo_means.append(geo_mean)
            else:
                geo_means.append(0)
        return geo_means

    def calculate_f_value(self):
        @self.sort_columns_decorator
        def calculate():
            geo_means = self.geometric_mean_below_diag()
            total_sum = 0
            for mean in geo_means:
                total_sum += mean
            return total_sum

        return calculate()


matrix_data = [
    [9, 24, -2, 86, -3],
    [40, 49, -4, 3, 0],
    [27, -76, 77, -1, 69],
    [71, -89, 94, -51, 50],
    [2, 96, 42, 36, -1]
]

matrix = Matrix(matrix_data)

matrix.print_matrix("Оригінальна матриця:")

F_value = matrix.calculate_f_value()

matrix.print_matrix("Відсортована матриця:")
print("Значення функції f(aij) (середнє геометричне):", matrix.geometric_mean_below_diag())
print("Значення функції F(fi(aij)):", F_value)
