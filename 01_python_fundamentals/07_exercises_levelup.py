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
# Level Up — Integrated Exercises

Goal: move from isolated skills → real workflow.

You will:

- build a dataset
- transform it
- analyze it
- construct a kernel (GP idea)

👉 Less guidance, more thinking.
"""
    )
    return


# --- TOGGLE ---

@app.cell
def _(mo):
    show_solution = mo.ui.switch(value=False, label="Show solutions")
    return show_solution


# =========================================
# 🟢 STEP 1 — DATA GENERATION
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Step 1 — Generate a dataset

Simulate a time series:

- time = 0..99
- signal = sin(time / 10)
- noise = random
- value = signal + noise

👉 Store in a DataFrame
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(np, pd, show_solution):
    if show_solution.value:
        time = np.arange(100)
        signal = np.sin(time / 10)
        noise = 0.3 * np.random.randn(100)

        value = signal + noise

        df = pd.DataFrame({
            "time": time,
            "signal": signal,
            "value": value
        })

        print(df.head())
    return


# =========================================
# 🟡 STEP 2 — FEATURE ENGINEERING
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Step 2 — Feature engineering

From your dataset:

- create value_squared
- create abs_value

👉 store in new columns
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(np, pd, show_solution):
    if show_solution.value:
        time = np.arange(100)
        signal = np.sin(time / 10)
        noise = 0.3 * np.random.randn(100)
        value = signal + noise

        df = pd.DataFrame({"time": time, "value": value})

        df["value_squared"] = df["value"]**2
        df["abs_value"] = df["value"].abs()

        print(df.head())
    return


# =========================================
# 🔵 STEP 3 — FILTERING & ANALYSIS
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Step 3 — Filtering

Keep only "large" values:

value_squared > 0.5

👉 How many rows remain?
"""
    )
    return


@app.cell
def _():
    # YOUR CODE HERE
    pass


@app.cell(hide_code=True)
def _(np, pd, show_solution):
    if show_solution.value:
        time = np.arange(100)
        signal = np.sin(time / 10)
        noise = 0.3 * np.random.randn(100)
        value = signal + noise

        df = pd.DataFrame({"time": time, "value": value})
        df["value_squared"] = df["value"]**2

        df_filt = df[df["value_squared"] > 0.5]

        print("Remaining rows:", len(df_filt))
    return


# =========================================
# 🔴 STEP 4 — DISTANCE STRUCTURE
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Step 4 — Distances (core modeling step)

Take your time variable:

1. compute pairwise differences
2. square them

👉 This prepares kernel computation
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
        t = np.arange(100)

        diff = np.subtract.outer(t, t)
        dist2 = diff**2

        print(dist2.shape)
    return


# =========================================
# 🟣 STEP 5 — KERNEL CONSTRUCTION
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Step 5 — Kernel

Compute:

kernel = exp(-distance / scale)

Try scale = 100

👉 What does the matrix look like?
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
        t = np.arange(100)

        diff = np.subtract.outer(t, t)
        dist2 = diff**2

        kernel = np.exp(-dist2 / 100)

        print(kernel)
    return


# =========================================
# 🔵 STEP 6 — VISUALIZATION
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Step 6 — Visualization

1. plot value (scatter)
2. plot signal (line)
3. visualize kernel matrix (imshow)

👉 Connect data ↔ structure
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
        t = np.arange(100)
        signal = np.sin(t / 10)
        noise = 0.3 * np.random.randn(100)
        value = signal + noise

        # data plot
        plt.scatter(t, value, label="data")
        plt.plot(t, signal, color="red", label="signal")
        plt.legend()
        plt.show()

        # kernel
        diff = np.subtract.outer(t, t)
        kernel = np.exp(-diff**2 / 100)

        plt.imshow(kernel)
        plt.title("Kernel matrix")
        plt.colorbar()
        plt.show()
    return


# =========================================
# 🔥 FINAL STEP — FUNCTIONALIZATION
# =========================================

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## Final — Build reusable code

Create a function:

build_kernel(x, scale)

👉 returns kernel matrix

Test with different scales.

👉 How does it change?
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
        def build_kernel(x, scale=1.0):
            diff = np.subtract.outer(x, x)
            return np.exp(-diff**2 / scale)

        x = np.linspace(0, 10, 50)

        k1 = build_kernel(x, scale=1)
        k2 = build_kernel(x, scale=50)

        print("Different scales → different smoothness")
    return


# --- SUMMARY ---

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
## ✅ What you just did

You combined:

- data simulation
- transformations
- filtering
- distances
- kernels
- visualization
- reusable functions

👉 This is 80% of what happens inside Gaussian Processes.

You are now ready for probabilistic modeling.
"""
    )
    return


if __name__ == "__main__":
    app.run()