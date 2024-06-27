import pandas as pd

file = "data.csv"

data = pd.read_csv(file, parse_dates=["REF_DATE"])

# only keep data that has an associated province
data = data[data["GEO"] != 'Canada']

# before grouping by these, drop the NaN rows
data = data.dropna(subset=["GEO", "Traveller characteristics", "VALUE"])

data = data.drop_duplicates()

def extract_month_year(dateobj):
    return f"{dateobj.year}-{dateobj.month}"

def get_quarter(dateobj):
    return f"{dateobj.year}-Q{((dateobj.month-1)//3)+1}"

def get_mode_of_transport(characteristics):
    if 'air' in characteristics.lower():
        return 'air'
    elif 'land' in characteristics.lower():
        return 'land'
    elif 'water' in characteristics.lower():
        return 'water'
    elif 'other modes' in characteristics.lower():
        return 'other modes'
    else:
        return 'unknown'

data["month-year"] = data["REF_DATE"].apply(extract_month_year)

data["quarter"] = data["REF_DATE"].apply(get_quarter)

data["mode of transport"] = data["Traveller characteristics"].apply(get_mode_of_transport)

selected_columns = ["REF_DATE", "GEO", "Traveller characteristics", "Traveller type", "VALUE", "month-year", "quarter", "mode of transport"]

data = data[selected_columns]

print(data["Traveller type"].unique())

data = data[data["Traveller type"] != "Travellers"]

data.to_csv("cleaned_data.csv")