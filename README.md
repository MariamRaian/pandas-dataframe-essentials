# pandas DataFrame Essentials

A small Python learning project using employee and product tables to practice the core steps of working with pandas DataFrames: create a table, select data, add a column, and remove rows or columns.

Developed from a club assignment. The focus is clear, step-by-step table operations, not a full data analysis or business application.

## Two worked examples

### Employee table

- Build a five-row DataFrame from names, jobs, and salaries.
- Select a column, a labeled row, and one salary value with `.loc`.
- Add a department column.
- Drop the job column and the row labeled `4`.

### Product table

- Build a four-row DataFrame from categories, brands, and prices.
- Select a brand column, a labeled row, and one price value.
- Add the exercise's supplied tax values.
- Drop the brand column and the row labeled `2`.

Tax values are entered directly, not calculated. The example does not apply a tax policy or specify a currency. Data is embedded in the script and used only for practice; it is not presented as a verified business dataset.

## Run locally

Requires Python 3 and pandas.

```bash
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Then install and run:

```bash
python -m pip install -r requirements.txt
python dataframe_operations.py
```

Use `python3` instead of `python` if that is your system's Python 3 command. Each step prints a labeled result. For example, the selected employee salary is `9000` and the selected product price is `8000`.

## Files

| File | Purpose |
| --- | --- |
| `dataframe_operations.py` | Both worked examples, organized into two functions |
| `requirements.txt` | pandas dependency |

## Skills demonstrated

- Creating DataFrames from dictionaries
- Selecting Series, rows, and scalar values
- Using label-based `.loc` access
- Assigning a new column
- Dropping rows and columns with explicit axes
- Reading table output and following transformations

## Scope and preparation

This is an introductory pandas exercise, not a dashboard, prediction model, or completed exploratory analysis. Preparation fixed a stray indentation error, removed duplicate setup, corrected spelling/capitalization in labels, and replaced notebook-only expressions with labeled prints. The original table operations and numeric values are retained. No new analysis or product features were added.
