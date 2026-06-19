import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Environment Check ✅

    This notebook verifies that your Python environment is correctly set up.
    """)
    return


@app.cell
def _():
    import sys
    print("Python version:", sys.version)
    return


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("NumPy:", np.__version__)
    print("Pandas:", pd.__version__)
    return np, plt


@app.cell
def _(np, plt):
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.plot(x, y)
    plt.title("Test plot")
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("""
    ## ✅ If you see a curve above:

    Your environment is working correctly.

    You are ready to start the course.
    """)
    return


if __name__ == "__main__":
    app.run()
