import pandas as pd

# Writing to a CSV file
df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
print(df)
df.to_csv("output.csv", index=False)

# Reading from a CSV file
df = pd.read_csv("output.csv")
print(df)

