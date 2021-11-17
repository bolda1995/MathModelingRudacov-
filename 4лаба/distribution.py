from numpy.random import gamma, normal, poisson
import random


class EvenDistribution:                         # - нужно для генератора
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def generate(self):
        return self.a + (self.b - self.a) * random.random()


class PoissonDistribution:                      # - нужно для обслуживающего аппарата
    def __init__(self, k: float, lambd: float):
        self.k = k
        self.lambd = lambd

    def generate(self):
        return poisson(self.lambd, self.k)


class GammaDistribution:                        # - не нужно, но хороший код, пусть будет
    def __init__(self, k, theta):
        self.k = k
        self.theta = theta

    def generate(self):
        return gamma(self.k, self.theta)


class NormalDistribution:                       # - не нужно, но хороший код, пусть будет
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def generate(self):
        return normal(self.mu, self.sigma)
