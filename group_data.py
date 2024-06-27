import pandas as pd

file = "cleaned_data.csv"

data = pd.read_csv(file)

# grouped datasets
grouped_data_trav_num_and_type = data.groupby(["GEO", "Traveller characteristics"]).agg({"VALUE":"sum"})

grouped_data_trav_num_and_type_quarter = data.groupby(["GEO", "Traveller characteristics", "quarter"]).agg({"VALUE":"sum"})

grouped_data_trav_num_quarter = data.groupby(["GEO", "quarter"]).agg({"VALUE":"sum"})

grouped_data_trav_num_mode_quarter = data.groupby(["GEO", "mode of transport"]).agg({"VALUE":"sum"})

# to csv
grouped_data_trav_num_and_type.to_csv("grouped_data/grouped_data_trav_num_and_type.csv")

grouped_data_trav_num_and_type_quarter.to_csv("grouped_data/grouped_data_trav_num_and_type_quarter.csv")

grouped_data_trav_num_quarter.to_csv("grouped_data/grouped_data_trav_num_and_quarter.csv")

grouped_data_trav_num_mode_quarter.to_csv("grouped_data/grouped_data_trav_num_mode_quarter.csv")