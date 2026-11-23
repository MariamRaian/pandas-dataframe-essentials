"""Practice pandas selection and table edits with small example datasets."""

import pandas as pd


def employee_example():
    """Create an employee table, select values, and drop a column and row."""
    employees = {
        "name": ["Tamer", "Safaa", "Manal", "Mohamed", "Nour"],
        "job": ["engineer", "accountant", "specialist", "writer", "engineer"],
        "salary": [5000, 7000, 8000, 9000, 4500],
    }
    df = pd.DataFrame(employees)
    print("EMPLOYEE TABLE\n", df, sep="")
    print("\nJob column:\n", df["job"], sep="")
    print("\nRow labeled 3:\n", df.loc[3], sep="")
    print("\nSalary at row 3:", df.loc[3, "salary"])
    df["dept"] = ["sales", "it", "quality", "stock", "training"]
    print("\nWith departments:\n", df, sep="")
    df = df.drop(columns="job")
    print("\nAfter dropping job:\n", df, sep="")
    df = df.drop(index=4)
    print("\nAfter dropping row 4:\n", df, sep="")


def product_example():
    """Create a product table, add supplied tax values, and remove data."""
    products = {
        "categories": ["pc", "laptop", "monitor", "printer"],
        "brand": ["HP", "Dell", "Samsung", "Canon"],
        "price": [20000, 30000, 8000, 9000],
    }
    df = pd.DataFrame(products)
    print("\nPRODUCT TABLE\n", df, sep="")
    print("\nBrand column:\n", df["brand"], sep="")
    print("\nRow labeled 3:\n", df.loc[3], sep="")
    print("\nPrice at row 2:", df.loc[2, "price"])
    # These are the exercise's supplied values, not a tax calculation.
    df["tax"] = [2000, 3000, 800, 900]
    print("\nWith supplied tax values:\n", df, sep="")
    df = df.drop(columns="brand")
    print("\nAfter dropping brand:\n", df, sep="")
    print("\nRow labeled 0:\n", df.loc[0], sep="")
    df = df.drop(index=2)
    print("\nAfter dropping row 2:\n", df, sep="")


if __name__ == "__main__":
    employee_example()
    product_example()
