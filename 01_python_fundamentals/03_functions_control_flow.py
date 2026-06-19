import marimo

__generated_with = "0.23.6"
app = marimo.App()


# --- GLOBAL IMPORTS (BEST PRACTICE) ---

@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


# --- TITLE ---

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
# Functions & Control Flow

Goal: structure your code.

👉 This is critical for:
- writing reusable code
- building models (PyMC)
- avoiding copy/paste chaos

We focus on:
- functions
- simple logic (if / for)
"""
    )
    return


# --- SOLUTION TOGGLE ---

@app.cell
def _(mo):
    show_solution = mo.ui.switch(value=False, label="Show solutions")
    return show_solution


# --- FUNCTIONS BASICS ---

@app.cell
def _():
    def add(a, b):
        return a + b

    print(add(2, 3))
    return add


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
👉 A function:

input → transformation → output

This is the core pattern of all models.
"""
    )
    return


# --- FUNCTION WITH ARRAY ---

@app.cell
def _(add, np):
    arr = np.array([1, 2, 3])
    result = add(arr, 10)

    print(result)
    return arr


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
👉 Same function works with scalars AND arrays.

This is key in scientific computing.
"""
    )
    return


# --- MULTI-STEP FUNCTION ---

@app.cell
def _(np):
    def square_and_exp(x):
        return np.exp(x**2)

    x = np.linspace(0, 2, 5)

    print(square_and_exp(x))
    return square_and_exp


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
👉 Functions combine steps.

Very similar to what happens inside models.
"""
    )
    return


# --- IF CONDITION ---

@app.cell
def _():
    value = 10

    if value > 5:
        print("Greater than 5")
    else:
        print("Small number")

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
👉 Basic control logic.

Used for filtering, branching, debugging.
"""
    )
    return


# --- LOOP (minimal) ---

@app.cell
def _():
    values = [1, 2, 3]

    for v in values:
        print(v * 2)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
👉 Loops exist, but prefer NumPy when possible.
"""
    )
    return


# --- KEY PATTERN: FUNCTION AS MODEL BLOCK ---

@app.cell
def _(np):
    def compute_kernel(x):
        diff = np.subtract.outer(x, x)
        return np.exp(-diff**2)

    x = np.linspace(0, 3, 4)

    print(compute_kernel(x))
    return compute_kernel


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
🔥 IMPORTANT

Encapsulating logic into functions = clean modeling.

This is exactly how PyMC code is structured.
"""
    )
    return


# --- EXERCISE 1 ---

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Exercise 1

Create a function:

double(x)

that multiplies input by 2.

Test it with:
- a number
- a NumPy array
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(show_solution, np):
    if show_solution.value:
        def double(x):
            return x * 2

        print(double(5))
        print(double(np.array([1, 2, 3])))
    return


# --- EXERCISE 2 ---

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Exercise 2

Create a function:

compute_distance(x)

that:
1. computes pairwise differences
2. squares them

👉 return the distance matrix
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(show_solution, np):
    if show_solution.value:
        def compute_distance(x):
            diff = np.subtract.outer(x, x)
            return diff**2

        x = np.linspace(0, 3, 4)
        print(compute_distance(x))
    return


# --- SUMMARY ---

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## ✅ Summary

- functions = reusable logic
- control flow = simple decisions
- combine both → clean code

👉 You are now ready to handle real data.
"""
    )
    return


if __name__ == "__main__":
    app.run()