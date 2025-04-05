import polars as pl
# Reading from a CSV file
df = pl.read_csv("input.csv")
# Writing to a CSV file
df.write_csv("output.csv")


