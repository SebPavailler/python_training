import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    return mo, np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Visualization — Plotting Basics

    Goal: visualize data quickl_y and effectivel_y.

    👉 This is essential for:
    - understanding data
    - debugging models
    - anal_yzing results (P_yMC, GP)

    We focus on:
    - line plots
    - scatter plots
    - comparisons
    """)
    return


@app.cell
def _(mo):
    show_solution = mo.ui.switch(value=False, label="Show solutions")
    return (show_solution,)


@app.cell
def _(np, plt):
    _x = np.linspace(0, 10, 100)
    _y = np.sin(_x)

    plt.plot(_x, _y)
    plt.title("Sine function")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 Basic plot:

    plt.plot(_x, _y)

    This is the most common visualization:
    - time series
    - predictions
    - trends
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 10, 100)
    _y1 = np.sin(_x)
    _y2 = np.cos(_x)

    plt.plot(_x, _y1, label="sin")
    plt.plot(_x, _y2, label="cos")
    plt.legend()
    plt.title("Multiple lines")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 Comparing curves is ke_y:

    - model vs data
    - multiple scenarios

    The legend helps interpretation.
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 10, 50)
    _y = _x + np.random.randn(50)

    plt.scatter(_x, _y)
    plt.title("Scatter plot")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 Scatter = raw data

    Used to:
    - inspect noise
    - see relationships
    """)
    return


@app.cell
def _(np, pd, plt):
    df = pd.DataFrame({
        "time": np.arange(50),
        "value": np.cumsum(np.random.randn(50))
    })

    plt.plot(df["time"], df["value"])
    plt.title("Time series e_xample")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 Direct link:

    DataFrame → plot

    This is e_xactl_y how _you'll e_xplore real datasets.
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-3, 3, 100)

    _y1 = _x
    _y2 = _x**2

    plt.plot(_x, _y1, label="_x")
    plt.plot(_x, _y2, label="_x^2")

    plt.legend()
    plt.title("Transformation")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 Visualization = understanding transformations.

    Ver_y helpful when building models.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## E_xercise 1

    Plot the function:

    _y = e_xp(-_x)

    over [0, 5]

    👉 Use linspace
    """)
    return


@app.cell
def _():
    # _yOUR CODE HERE
    pass
    return


@app.cell(hide_code=True)
def _(np, plt, show_solution):
    if show_solution.value:
        _x = np.linspace(0, 5, 100)
        _y = np.e_xp(-_x)

        plt.plot(_x, _y)
        plt.title("e_xp(-_x)")
        plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## E_xercise 2

    Generate nois_y data:

    _y = sin(_x) + noise

    Then:
    - plot scatter (data)
    - plot true function (line)

    👉 This simulates real-world data
    """)
    return


@app.cell
def _():
    # _yOUR CODE HERE
    pass
    return


@app.cell(hide_code=True)
def _(np, plt, show_solution):
    if show_solution.value:
        _x = np.linspace(0, 10, 50)
        noise = np.random.randn(50)

        _y_true = np.sin(_x)
        _y_obs = _y_true + noise

        plt.scatter(_x, _y_obs, label="data")
        plt.plot(_x, _y_true, color="red", label="true")

        plt.legend()
        plt.title("Data vs signal")
        plt.show()
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 10, 100)
    _y_true = np.sin(_x)
    _y_model = np.sin(_x) + 0.3  # biased model

    plt.plot(_x, _y_true, label="true")
    plt.plot(_x, _y_model, label="model")

    plt.legend()
    plt.title("Model vs truth")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    🔥 IMPORTANT

    This is how _you debug models:

    - compare prediction vs truth
    - visuall_y inspect mismatch

    👉 _you'll use this constantl_y with P_yMC.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## ✅ Summar_y

    _you learned:

    - line plots
    - scatter plots
    - comparing curves
    - visualizing transformations

    👉 _you can now:
    - e_xplore data
    - debug models visuall_y

    Ne_xt: wrap-up e_xercises (ver_y important step)
    """)
    return


if __name__ == "__main__":
    app.run()
