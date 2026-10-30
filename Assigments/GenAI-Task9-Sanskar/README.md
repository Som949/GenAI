# NumPy Fundamentals Assignment

This repository contains seven Python tasks covering the basics of NumPy arrays, mathematical operations, aggregation, statistics, sorting, percentiles, and a simple sales analysis.

## Tasks Covered

| File | Topics |
|---|---|
| `task1.py` | Creating 1D and 2D NumPy arrays, checking array shape and data type |
| `task2.py` | Array addition, subtraction, multiplication, division, and power |
| `task3.py` | Square root, exponential, natural logarithm, sum, and cumulative sum |
| `task4.py` | Row-wise and column-wise sums, minimum, maximum, and mean of a 2D array |
| `task5.py` | Mean, median, variance, standard deviation, minimum, maximum, and range |
| `task6.py` | Sorting, percentiles, and counting marks above the average |
| `task7.py` | Weekly sales total, average, highest/lowest sales day, standard deviation, and above-average sales |

## Requirements

- Python 3.8 or newer
- NumPy

Only NumPy is required for these tasks. Pandas and Matplotlib are not used.

## Setup

### 1. Open the project directory

Open a terminal in the folder containing `task1.py` through `task7.py`.

### 2. Create and activate a virtual environment

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install NumPy

```bash
python -m pip install numpy
```

If your system uses `python3` instead of `python`, run:

```bash
python3 -m pip install numpy
```

## Run the Tasks

Run each task separately from the project directory.

```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
python task6.py
python task7.py
```

On systems where the Python command is `python3`, use `python3 task1.py`, and similarly for the other files.

## Example

To run the sales analysis:

```bash
python task7.py
```

The script prints the total and average sales, the indices of the highest- and lowest-sales days, the standard deviation, and the number of days with sales above average.

> Day numbers in the output may be zero-based if the script uses NumPy's `argmax()` and `argmin()` directly. Add `1` to those indices if you want to display days as Day 1 through Day 7.
