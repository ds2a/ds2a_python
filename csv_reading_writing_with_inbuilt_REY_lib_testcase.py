import ray
import pandas as pd
ray.init(ignore_reinit_error=True)

# Reading and processing CSV files in parallel
@ray.remote
def process_csv(file_name):
    return pd.read_csv(file_name)

# Process CSV in parallel
files = ["output.csv", "output.csv"]
results = ray.get([process_csv.remote(f) for f in files])
# You can now process the results further as needed
print(results)

