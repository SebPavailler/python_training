import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd

    return mo, np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # DataFrames — Pandas Basics

    Goal: work with tabular data.

    👉 This is essential for:
    - real datasets
    - time series (SSM)
    - model inputs (PyMC)

    We focus on:
    - selecting data
    - filtering
    - simple transformations
    """)
    return


@app.cell
def _(mo):
    show_solution = mo.ui.switch(value=False, label="Show solutions")
    return (show_solution,)


@app.cell
def _(np, pd):
    data = {
        "time": np.arange(10),
        "value": np.random.randn(10),
    }

    df = pd.DataFrame(data)
    print(df.head())
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 DataFrame = table (rows + columns)

    Very similar to:
    - Excel
    - SQL tables

    Everything you do later starts here.
    """)
    return


@app.cell
def _(df):
    print(df["value"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 Select a column:

    df["column_name"]

    👉 This is used constantly.
    """)
    return


@app.cell
def _(df):
    _filtered = df[df["value"] > 0]
    print(_filtered)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 Filtering = selecting rows based on a condition

    df[df["value"] > 0]

    👉 This is critical for real data cleaning.
    """)
    return


@app.cell
def _(df):
    df2 = df.copy()
    df2["value_squared"] = df2["value"] ** 2

    print(df2.head())
    return (df2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 You can create new columns easily.

    Used for:
    - feature engineering
    - transformations
    """)
    return


@app.cell
def _(df):
    import matplotlib.pyplot as plt

    plt.plot(df["time"], df["value"])
    plt.title("Time series")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    👉 DataFrames connect directly to visualization.

    This is how you inspect your data before modeling.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 1

    Create a new column:

    "value_abs" = absolute value of "value"

    Then:
    - print the first rows
    """)
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass
    return


@app.cell(hide_code=True)
def _(df, show_solution):
    if show_solution.value:
        df_sol = df.copy()
        df_sol["value_abs"] = df_sol["value"].abs()
        print(df_sol.head())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 2

    Filter the dataset:

    Keep only rows where:
    "value_squared" > 1

    👉 Hint:
    You may need the transformed dataframe
    """)
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass
    return


@app.cell(hide_code=True)
def _(df2, show_solution):
    if show_solution.value:
        filtered = df2[df2["value_squared"] > 1]
        print(filtered)
    return


@app.cell
def _(df):
    df_pipe = df.copy()
    df_pipe["value_squared"] = df_pipe["value"] ** 2

    result = df_pipe[df_pipe["value_squared"] > 1]

    print(result.head())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    🔥 IMPORTANT

    This is a typical data workflow:

    1. start with data
    2. transform
    3. filter
    4. use result

    👉 This pattern appears everywhere in real projects.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## ✅ Summary

    You learned:

    - DataFrame basics
    - column selection
    - filtering
    - transformations

    👉 You can now manipulate real data.

    Next step:
    visualization (more structured)
    """)
    return


if __name__ == "__main__":
    app.run()
