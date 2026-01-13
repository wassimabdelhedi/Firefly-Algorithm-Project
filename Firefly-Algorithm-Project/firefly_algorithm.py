import random
import math

class FireflyAlgorithm:
    def __init__(self, func, n_fireflies=15, max_gen=50, alpha=0.5, beta0=1, gamma=1, delta=0.97):
        self.func = func
        self.n = n_fireflies
        self.MaxGen = max_gen
        self.alpha = alpha
        self.beta0 = beta0
        self.gamma = gamma
        self.delta = delta

        # Initial positions
        self.fireflies = [random.uniform(-10, 10) for _ in range(self.n)]
        self.history = []

    # Light intensity (for minimization problem)
    def intensity(self, x):
        return -self.func(x)

    # Distance in 1D
    def distance(self, xi, xj):
        return abs(xi - xj)

    # Move firefly i towards j
    def move_firefly(self, i, j):
        r = self.distance(self.fireflies[i], self.fireflies[j])
        beta = self.beta0 * math.exp(-self.gamma * r ** 2)
        self.fireflies[i] += beta * (self.fireflies[j] - self.fireflies[i]) + self.alpha * (random.random() - 0.5)

    # Run algorithm
    def run(self):
        alpha = self.alpha
        for t in range(self.MaxGen):
            for i in range(self.n):
                for j in range(self.n):
                    if self.intensity(self.fireflies[j]) > self.intensity(self.fireflies[i]):
                        self.move_firefly(i, j)

            # Update light intensities
            self.history.append(min([self.func(x) for x in self.fireflies]))
            # Reduce randomness
            alpha *= self.delta

        # Best solution
        best_index = min(range(self.n), key=lambda i: self.func(self.fireflies[i]))
        self.best_solution = self.fireflies[best_index]
        return self.best_solution, self.history
