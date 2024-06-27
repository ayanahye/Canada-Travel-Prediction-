import pandas as pd

file = "data.csv"

data = pd.read_csv(file, parse_dates=["REF_DATE"])

# only keep data that has an associated province
data = data[data["GEO"] != 'Canada']

# before grouping by these, drop the NaN rows
data = data[~data["GEO"].isna()]
data = data[~data["Traveller characteristics"].isna()]

def extract_month_year(dateobj):
    return f"{dateobj.year}-{dateobj.month}"

def get_quarter(dateobj):
    return f"{dateobj.year}-Q{((dateobj.month-1)//3)+1}"

data["month-year"] = data["REF_DATE"].apply(extract_month_year)

data["quarter"] = data["REF_DATE"].apply(get_quarter)

# get the total number of travelers for each province by their characteristic
grouped_data_trav_num_and_type = data.groupby(["GEO", "Traveller characteristics"]).agg({"VALUE":"sum"})

grouped_data_trav_num_and_type_quarter = data.groupby(["GEO", "Traveller characteristics", "quarter"]).agg({"VALUE":"sum"})

grouped_data_trav_num_quarter = data.groupby(["GEO", "quarter"]).agg({"VALUE":"sum"})

# grouped_data_trav_num_and_type_month = data.groupby(["GEO", "Traveller characteristics", "month-year"]).agg({"VALUE":"sum"})

grouped_data_trav_num_and_type.to_csv("grouped_data_trav_num_and_type.csv")

# grouped_data_trav_num_and_type_month.to_csv("grouped_data_trav_num_and_type_month.csv")

grouped_data_trav_num_and_type_quarter.to_csv("grouped_data_trav_num_and_type_quarter.csv")

grouped_data_trav_num_quarter.to_csv("grouped_data_trav_num_and_quarter.csv")
# print(grouped_data_trav_num_and_type.to_string())

print(grouped_data_trav_num_quarter.to_string())