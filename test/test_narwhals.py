import narwhals as nw
from narwhals.typing import FrameT

@nw.narwhalify
def func(df: FrameT) -> FrameT:
    return df.with_columns(
        nw.col("a") + nw.col("b").alias("jumlah")
    )

if __name__ == "__main__":
    import polars as pl
    import pandas as pd
    df = pl.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    })
    df_pd = pd.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    })
    df_lazy = pl.LazyFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    })
    print(func(df))
    print(func(df_pd))
    print(func(df_lazy).collect())