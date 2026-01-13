import matplotlib.pyplot as plt
import os

# Convergence curve
def plot_convergence(history):
    os.makedirs("results/convergence_plots", exist_ok=True)
    plt.figure()
    plt.plot(history, marker='o')
    plt.xlabel("Iteration")
    plt.ylabel("Best Fitness")
    plt.title("Firefly Algorithm Convergence")
    plt.grid(True)
    plt.savefig("results/convergence_plots/convergence_curve.png")
    plt.close()

# Optimization landscape with fireflies
def plot_landscape(f, fireflies, x_range=(-10,10), resolution=400):
    os.makedirs("results/optimization_landscape", exist_ok=True)

    import numpy as np
    X = np.linspace(x_range[0], x_range[1], resolution)
    Y = [f(xi) for xi in X]

    plt.figure()
    plt.plot(X, Y, label="f(x)")
    plt.scatter(fireflies, [f(x) for x in fireflies],
                color='yellow', edgecolors='black', label="Fireflies")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Optimization Landscape")
    plt.legend()
    plt.grid(True)
    plt.savefig("results/optimization_landscape/landscape.png")
    plt.close()
