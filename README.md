# Python Training for Bayesian Workflow

A hands-on repository for ramping up on Python, Bayesian workflows, and PyMC.

---

## Setup

1. Clone the repo:  
   ```bash
   git clone https://github.com/your-username/python_training.git
   cd python_training
   ```

2. Install dependencies (Pixi required):  
   ```bash
   pixi install
   ```

3. Verify PyMC:  
   ```bash
   pixi run python -c "import pymc as pm; print(pm.__version__)"
   ```

---
## Open a Notebook
To start Week 1:  
```bash
pixi run workshop week1/notebooks/week1_python_refresher.marimo
```

---
## Course Outline
- Week 1: Python Refresher (NumPy, Polars, Plotting)
- Week 2: Probability & Simulation
- Week 3: PyMC Basics
- Week 4: Model Checking & Regression
- Week 5: GLMs & Hierarchical Models
- Week 6: Time Series & Causal Inference
- Week 7: Gaussian Processes
- Week 8: Capstone Project