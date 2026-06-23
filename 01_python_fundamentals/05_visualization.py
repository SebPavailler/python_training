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
# Visualization — Plotting Basics

Goal: visualize data quickly and effectively.

👉 This is essential for:
- understanding data
- debugging models
- analyzing results (PyMC, GP)

We focus on:
- line plots
- scatter plots
- comparisons
"""
    )
    return


# --- SOLUTION TOGGLE ---

@app.cell
def _(mo):
    show_solution = mo.ui.switch(value=False, label="Show solutions")
    return show_solution


# --- SIMPLE LINE PLOT ---

@app.cell
def _(np, plt):
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.plot(x, y)
    plt.title("Sine function")
    plt.show()
    return x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
👉 Basic plot:

plt.plot(x, y)

This is the most common visualization:
- time series
- predictions
- trends
"""
    )
    return


# --- MULTIPLE LINES ---

@app.cell
def _(x, np, plt):
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label="sin")
    plt.plot(x, y2, label="cos")
    plt.legend()
    plt.title("Multiple lines")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
👉 Comparing curves is key:

- model vs data
- multiple scenarios

The legend helps interpretation.
"""
    )
    return


# --- SCATTER PLOT ---

@app.cell
def _(np, plt):
    x = np.linspace(0, 10, 50)
    y = x + np.random.randn(50)

    plt.scatter(x, y)
    plt.title("Scatter plot")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
👉 Scatter = raw data

Used to:
- inspect noise
- see relationships
"""
    )
    return


# --- DATAFRAME PLOT ---

@app.cell
def _(pd, np, plt):
    df = pd.DataFrame({
        "time": np.arange(50),
        "value": np.cumsum(np.random.randn(50))
    })

    plt.plot(df["time"], df["value"])
    plt.title("Time series example")
    plt.show()
    return df


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
👉 Direct link:

DataFrame → plot

This is exactly how you'll explore real datasets.
"""
    )
    return


# --- TRANSFORMATION VISUALIZATION ---

@app.cell
def _(np, plt):
    x = np.linspace(-3, 3, 100)

    y1 = x
    y2 = x**2

    plt.plot(x, y1, label="x")
    plt.plot(x, y2, label="x^2")

    plt.legend()
    plt.title("Transformation")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
👉 Visualization = understanding transformations.

Very helpful when building models.
"""
    )
    return


# --- EXERCISE 1 ---

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Exercise 1

Plot the function:

y = exp(-x)

over [0, 5]

👉 Use linspace
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
        x = np.linspace(0, 5, 100)
        y = np.exp(-x)

        plt.plot(x, y)
        plt.title("exp(-x)")
        plt.show()
    return


# --- EXERCISE 2 ---

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Exercise 2

Generate noisy data:

y = sin(x) + noise

Then:
- plot scatter (data)
- plot true function (line)

👉 This simulates real-world data
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

        plt.scatter(x, y_obs, label="data")
        plt.plot(x, y_true, color="red", label="true")

        plt.legend()
        plt.title("Data vs signal")
        plt.show()
    return


# --- IMPORTANT PATTERN (MODEL DEBUG) ---

@app.cell
def _(np, plt):
    x = np.linspace(0, 10, 100)
    y_true = np.sin(x)
    y_model = np.sin(x) + 0.3  # biased model

    plt.plot(x, y_true, label="true")
    plt.plot(x, y_model, label="model")

    plt.legend()
    plt.title("Model vs truth")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
🔥 IMPORTANT

This is how you debug models:

- compare prediction vs truth
- visually inspect mismatch

👉 You'll use this constantly with PyMC.
"""
    )
    return


# --- SUMMARY ---

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## ✅ Summary

You learned:

- line plots
- scatter plots
- comparing curves
- visualizing transformations

👉 You can now:
- explore data
- debug models visually

Next: wrap-up exercises (very important step)
"""
    )
    return


if __name__ == "__main__":
    app.run()