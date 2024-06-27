import pandas as pd

file = "grouped_data_trav_num_and_type_month.csv"
data = pd.read_csv(file)

print(data[data["GEO"] == "Yukon"].to_string())