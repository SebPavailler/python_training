import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return mo


@app.cell
def _(mo):
    mo.md(
        """
# Python Fundamentals — Variables & Types

Goal: get comfortable reading and writing basic Python.

This notebook focuses only on:
- variables
- types
- lists & dictionaries
- indexing

👉 These are everywhere in NumPy, pandas, PyMC.
"""
    )
    return


# --- Variables ---

@app.cell
def _():
    x = 10
    y = 3.5
    name = "python"

    print(x, type(x))
    print(y, type(y))
    print(name, type(name))
    return


@app.cell
def _(mo):
    mo.md(
        """
👉 Python is dynamically typed:

- no need to declare types
- type inferred automatically

You will constantly manipulate:
- numbers
- strings
- arrays (later)
"""
    )
    return


# --- Lists ---

@app.cell
def _():
    values = [1, 2, 3, 4, 5]

    print(values)
    return values


@app.cell
def _(values):
    print(values[0])      # first element
    print(values[-1])     # last element
    print(values[1:4])    # slicing
    return


@app.cell
def _(mo):
    mo.md(
        """
👉 VERY IMPORTANT

Indexing and slicing are used everywhere:

- NumPy arrays
- pandas DataFrames
- model inputs

If this is not automatic → everything feels hard later.
"""
    )
    return


# --- Dictionaries ---

@app.cell
def _():
    person = {
        "name": "Alice",
        "age": 30,
        "score": 95
    }

    print(person)
    return person


@app.cell
def _(person):
    print(person["name"])
    print(person["age"])
    return


@app.cell
def _(mo):
    mo.md(
        """
👉 Dictionaries = key-value storage

You will see:
- configs
- model parameters
- data structures

Example:
model_config["sigma"]
"""
    )
    return


# --- Simple operations ---

@app.cell
def _():
    a = 10
    b = 5

    print(a + b)
    print(a * b)
    print(a / b)
    return


# --- Exercise 1 (easy) ---

@app.cell
def _(mo):
    mo.md(
        """
## Exercise 1

Create a list of numbers from 1 to 10.

Then:
- print the first element
- print the last element
- print elements 3 to 6
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass

@app.cell
def _():
    values = list(range(1, 11))

    print("First:", values[0])
    print("Last:", values[-1])
    print("Slice 3–6:", values[2:6])
    return


# --- Exercise 2 (slightly harder) ---

@app.cell
def _(mo):
    mo.md(
        """
## Exercise 2

Create a dictionary describing a dataset:

- "name": "sales"
- "n_obs": 100
- "mean": 250.5

Then print each value separately.
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell
def _():
    dataset = {
        "name": "sales",
        "n_obs": 100,
        "mean": 250.5
    }

    print(dataset["name"])
    print(dataset["n_obs"])
    print(dataset["mean"])
    return


@app.cell
def _(mo):
    mo.md(
        """
## ✅ Summary

You now know how to:

- create variables
- work with lists
- use indexing & slicing
- manipulate dictionaries

👉 Next step: NumPy (this is where things become powerful)
"""
    )
    return


if __name__ == "__main__":
    app.run()