import pandas as pd
import matplotlib.pyplot as plt
import os

file = "grouped_data/grouped_data_trav_num_excur_tour.csv"

data = pd.read_csv(file)

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

num_provinces = data["GEO"].nunique()

fig, axs = plt.subplots(num_provinces, 1, figsize=(14, 8 * num_provinces))

for i, geo in enumerate(data["GEO"].unique()):
    province_data = data[data["GEO"] == geo]
    axs[i].bar(province_data["Traveller type"], province_data["VALUE"], color='b')
    axs[i].set_title(f"Type vs Number of Travellers in {geo}")
    axs[i].set_ylabel("Number of Travellers")
    axs[i].set_xlabel("Type")
    axs[i].set_xticks(range(len(province_data["Traveller type"])))
    axs[i].set_xticklabels(province_data["Traveller type"])
    axs[i].legend([geo], loc='upper right')


plt.savefig(f"{output_dir}/combined_histograms_excur_tour.png")



