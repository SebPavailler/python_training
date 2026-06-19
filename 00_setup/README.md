# Setup & Environment

This folder helps you verify that your Python environment is correctly configured.

---

## Requirements

- Pixi installed
- Repository cloned
- Dependencies installed with:

```
pixi install
```

---

## Run marimo

Start marimo:

```
pixi run marimo edit
```


Open the file:

00_setup/01_environment_check.py

---

## What to check

The notebook verifies:

- Python environment is working
- Core libraries (numpy, pandas, matplotlib) are installed
- marimo is functional

---

## Troubleshooting

If something fails:

- Run pixi install again
- Check your pixi.toml
- Restart your environment