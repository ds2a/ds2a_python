import dask.dataframe as dd
# Reading from a CSV file
df = dd.read_csv("output*.csv")
# Writing to a CSV file
df.to_csv("output11-*.csv", index=False)

