from firefly_algorithm import FireflyAlgorithm
from visualization import plot_convergence, plot_landscape
import os

# 1. Fonction objectif
def f(x):
    return x ** 2   # Exemple simple 1D

# 2. Paramètres
n = 15
MaxGen = 50
alpha = 0.5
beta0 = 1
gamma = 1
delta = 0.97

# 3. Exécution Firefly Algorithm
fa = FireflyAlgorithm(f, n_fireflies=n, max_gen=MaxGen, alpha=alpha, beta0=beta0, gamma=gamma, delta=delta)
best_solution, history = fa.run()

print("Best solution x =", best_solution)
print("Best fitness f(x) =", f(best_solution))

# 4. Export résultats
os.makedirs("results/solutions", exist_ok=True)
os.makedirs("results/logs", exist_ok=True)

with open("results/solutions/best_solution.txt", "w") as fsol:
    fsol.write(f"Best solution x = {best_solution}\n")
    fsol.write(f"Best fitness f(x) = {f(best_solution)}\n")

with open("results/logs/run_log.txt", "w") as log:
    log.write("Firefly Algorithm Execution Log\n")
    log.write(f"Number of fireflies: {n}\n")
    log.write(f"Max generations: {MaxGen}\n")
    log.write(f"Final best solution: {best_solution}\n")
    log.write(f"Final best fitness: {f(best_solution)}\n")

# 5. Graphiques
plot_convergence(history)
plot_landscape(f, fa.fireflies)
