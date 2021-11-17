import numpy
class FindProb:
    time_delta = 10e-3
    matrix = []
    len = 0
    def __init__(self, matr, len):
        self.matrix = matr
        self.len = len

    def build_coeff_matrix(self):# создание матриц коэфициентов систем уравнений колмогорова
        self.matrix = numpy.array(self.matrix)
        n = self.len
        res = numpy.zeros((n, n))
        for state in range(n - 1):
            for col in range(n):
                res[state, state] -= self.matrix[state, col]
            for row in range(n):
                res[state, row] += self.matrix[row, state]

        for state in range(n):
            res[n - 1, state] = 1

        return res

    def build_augmentation_matrix(self): # создание массива свободных коэфициентов
        res = [0 for i in range(self.len)]
        res[self.len - 1] = 1
        return numpy.array(res)

    def solve_probiliti(self): # нахождение придельных вероятностей решение через системы уравнений
        return numpy.linalg.solve(self.build_coeff_matrix(), self.build_augmentation_matrix())

    def dps(self, probabilities): # измение за время дельта т
        return [
            self.time_delta * sum(
                [
                    probabilities[j] * (-sum(self.matrix[i]) + self.matrix[i][i])
                    if i == j else
                    probabilities[j] * self.matrix[j][i]
                    for j in range(self.len)
                ]
            )
            for i in range(self.len)
        ]

    def calc_stabilization_times(self): # моделирование процессов стабилизациии вероятности системы
        current_time = 0
        limit_probabilities = self.solve_probiliti()
        current_probabilities = [1/self.len] * self.len
        stabilization_times = [0 for i in range(self.len)]

        total_lambda_sum = sum([sum(i) for i in self.matrix]) * 10
        cool_eps = [p / total_lambda_sum for p in limit_probabilities]

        while not all(stabilization_times):
            curr_dps = self.dps(current_probabilities)
            for i in range(self.len):
                if (not stabilization_times[i] and curr_dps[i] <= cool_eps[i] and
                        abs(current_probabilities[i] - limit_probabilities[i]) <= cool_eps[i]):
                    stabilization_times[i] = current_time
                current_probabilities[i] += curr_dps[i]

            current_time += self.time_delta

        return stabilization_times
