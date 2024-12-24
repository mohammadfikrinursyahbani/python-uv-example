import polars as pl
import duckdb

def jumlah(df):
    return df.with_columns(
        pl.col("a") + pl.col("b").alias("jumlah")
    )

if __name__ == "__main__":
    df = pl.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    })
    print(jumlah(df))
    print(duckdb.sql("SELECT * FROM df"))