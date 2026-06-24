import marimo

__generated_with = "0.23.6"
app = marimo.App()


# --- GLOBAL IMPORTS ---

@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, np, pd, plt


# --- TITLE ---

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
# Wrap-up Exercises — Python Fundamentals

Goal: consolidate all previous concepts.

👉 This notebook is critical:
- less guided
- more thinking
- real understanding

Sections:
1. basics
2. numpy
3. distances (GP core)
4. mini pipeline
"""
    )
    return


# --- TOGGLE ---

@app.cell
def _(mo):
    show_solution = mo.ui.switch(value=False, label="Show solutions")
    return show_solution


# =========================================
# 🟢 BLOCK 1 — BASICS
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md("## 🟢 Block 1 — Basics")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
Exercise 1:

Create a list from 1 to 10.

- print first element
- print last element
- print elements 4 to 7
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(show_solution):
    if show_solution.value:
        values = list(range(1, 11))
        print(values[0])
        print(values[-1])
        print(values[3:7])
    return


# =========================================
# 🟡 BLOCK 2 — NUMPY
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md("## 🟡 Block 2 — NumPy")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
Exercise 2:

Create an array from 0 to 5 (50 points)

- compute x²
- compute exp(-x)
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(np, show_solution):
    if show_solution.value:
        x = np.linspace(0, 5, 50)
        print(x**2)
        print(np.exp(-x))
    return


# =========================================
# 🔴 BLOCK 3 — DISTANCES (GP CORE)
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md("## 🔴 Block 3 — Distances (GP core)")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
Exercise 3:

Given:

x = np.linspace(0, 3, 5)

1. compute pairwise differences
2. square them
3. apply exp(-distance)

👉 This builds a kernel matrix
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(np, show_solution):
    if show_solution.value:
        x = np.linspace(0, 3, 5)
        diff = np.subtract.outer(x, x)
        dist2 = diff**2
        kernel = np.exp(-dist2)
        print(kernel)
    return


# =========================================
# 🔵 BLOCK 4 — FUNCTIONS
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md("## 🔵 Block 4 — Functions")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
Exercise 4:

Write a function:

compute_kernel(x)

that returns:

exp(-(x - x')²)
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(np, show_solution):
    if show_solution.value:
        def compute_kernel(x):
            diff = np.subtract.outer(x, x)
            return np.exp(-diff**2)

        x = np.linspace(0, 3, 5)
        print(compute_kernel(x))
    return


# =========================================
# 🟣 BLOCK 5 — DATA + PIPELINE
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md("## 🟣 Block 5 — Data pipeline")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
Exercise 5:

1. Create DataFrame:

time = 0..49  
value = random  

2. Add column value_squared  

3. Filter rows where value_squared > 1  

4. Plot result
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(np, pd, plt, show_solution):
    if show_solution.value:
        df = pd.DataFrame({
            "time": np.arange(50),
            "value": np.random.randn(50),
        })

        df["value_squared"] = df["value"]**2
        df_filt = df[df["value_squared"] > 1]

        plt.scatter(df_filt["time"], df_filt["value"])
        plt.title("Filtered data")
        plt.show()
    return


# =========================================
# 🔥 FINAL MINI PROJECT
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## 🔥 Final Exercise

Simulate a signal:

y = sin(x) + noise

Then:

1. plot noisy data (scatter)
2. plot true signal (line)
3. compute distance matrix on x
4. visualize kernel matrix

👉 You are combining EVERYTHING
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(np, plt, show_solution):
    if show_solution.value:
        x = np.linspace(0, 10, 50)
        noise = np.random.randn(50)

        y_true = np.sin(x)
        y_obs = y_true + noise

        # plot data
        plt.scatter(x, y_obs, label="data")
        plt.plot(x, y_true, color="red", label="true")
        plt.legend()
        plt.show()

        # kernel
        diff = np.subtract.outer(x, x)
        kernel = np.exp(-diff**2)

        plt.imshow(kernel)
        plt.title("Kernel matrix")
        plt.colorbar()
        plt.show()
    return


# --- SUMMARY ---

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## ✅ Summary

If you completed this:

✅ you are fluent in Python basics  
✅ NumPy is natural  
✅ functions are clear  
✅ you understand GP building blocks  

👉 You are ready for probabilistic programming.
"""
    )
    return


if __name__ == "__main__":
    app.run()