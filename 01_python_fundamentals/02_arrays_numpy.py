import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np

    return mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # NumPy — Arrays & Vectorization

    Goal: understand the core operations used in data & modeling.

    👉 This notebook is CRITICAL for:
    - PyMC
    - Gaussian Processes

    We focus on:
    - arrays
    - vectorization
    - distances (VERY important)
    """)
    return


@app.cell
def _(mo):
    show_solution = mo.ui.switch(value=False, label="Show solutions")
    return (show_solution,)


@app.cell
def _(np):
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    return (arr,)


@app.cell
def _(arr):
    print("First:", arr[0])
    print("Last:", arr[-1])
    print("Slice:", arr[1:4])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 Arrays behave like lists, but support fast math operations.

    Everything later (GP, PyMC) relies on this structure.
    """)
    return


@app.cell
def _(arr):
    print(arr + 1)
    print(arr * 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 Instead of loops:

    for i in arr:
    ...

    You write:

    arr + 1

    👉 This is called vectorization.
    """)
    return


@app.cell
def _(np):
    x_grid = np.linspace(0, 5, 5)
    print(x_grid)
    return (x_grid,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 linspace creates a grid of values.

    Used for:
    - plotting
    - simulations
    - defining input space (GP)
    """)
    return


@app.cell
def _(np, x_grid):
    diff = np.subtract.outer(x_grid, x_grid)
    print(diff)
    return (diff,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    🔥 IMPORTANT CONCEPT

    What does subtract.outer do?

    Given:
    x = [1, 2, 3]

    It computes ALL pairwise differences:

    [1-1, 1-2, 1-3
     2-1, 2-2, 2-3
     3-1, 3-2, 3-3]

    👉 Result = matrix of differences

    Why this matters:

    Gaussian Processes use:

    k(x, x') = exp(-(x - x')²)

    👉 So we need ALL (x - x')

    This line builds the core of GP kernels.
    """)
    return


@app.cell
def _(diff):
    dist2 = diff**2
    print(dist2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 We square the differences:

    (x - x')²

    This gives a distance matrix.

    👉 Then GP applies exponential:

    exp(-distance)

    👉 That’s the kernel.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 1

    Create a grid from 0 to 10 with 6 points.

    Then:
    - multiply it by 3
    - compute its square
    """)
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass
    return


@app.cell(hide_code=True)
def _(np, show_solution):
    if show_solution.value:
        x_sol = np.linspace(0, 10, 6)
        print(x_sol)
        print(x_sol * 3)
        print(x_sol ** 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 2

    Given a grid:

    x = np.linspace(0, 3, 4)

    1. Compute pairwise differences
    2. Square them
    3. Apply exp(-distance)

    👉 This builds a simple GP kernel
    """)
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass
    return


@app.cell(hide_code=True)
def _(kernel, np, show_solution):
    if show_solution.value:
        _x = np.linspace(0, 3, 4)
        _diff = np.subtract.outer(_x, _x)
        _dist2 = _diff**2
        _kernel = np.exp(-_dist2)

        print(kernel)
    return


@app.cell
def _(np):
    import matplotlib.pyplot as plt

    x = np.linspace(0, 5, 100)
    y = np.exp(-x**2)

    plt.plot(x, y)
    plt.title("Example: exp(-x^2)")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## ✅ Summary

    You now understand:

    - arrays
    - vectorization
    - pairwise differences
    - distance matrices
    - exponential kernels

    👉 You just built the core of Gaussian Processes.

    Next: structuring code (functions & control)
    """)
    return


if __name__ == "__main__":
    app.run()
