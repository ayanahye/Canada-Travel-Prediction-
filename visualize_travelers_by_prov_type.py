import pandas as pd
import matplotlib.pyplot as plt
import os

file = "grouped_data_trav_num_and_type.csv"
data = pd.read_csv(file)

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

characteristics = data["Traveller characteristics"].unique()
char_to_num = {char: num for num, char in enumerate(characteristics)}

print(char_to_num)

data["Characteristic_num"] = data["Traveller characteristics"].map(char_to_num)

'''
for geo in data["GEO"].unique():
    province_data = data[data["GEO"] == geo]
    plt.figure(figsize=(10, 6))
    plt.bar(province_data["Characteristic_num"], province_data["VALUE"], color='r')
    plt.xlabel("Traveller characteristics (Numbered)")
    plt.ylabel("Number of Travellers")
    plt.title(f"Traveller characteristics vs Number of Travellers in {geo}")

    #legend_labels = [f"{num}: {char}" for char, num in char_to_num.items()]
    #plt.legend(legend_labels, loc='upper left')

    plt.xticks(ticks=list(char_to_num.values()), labels=list(char_to_num.values()))
    
    plt.savefig(f"{output_dir}/{geo}_scatter_plot.png")

print(data)
'''

num_provinces = data["GEO"].nunique()

fig, axs = plt.subplots(num_provinces, 1, figsize=(14, 8 * num_provinces))

for i, geo in enumerate(data["GEO"].unique()):
    province_data = data[data["GEO"] == geo]
    axs[i].bar(province_data["Characteristic_num"], province_data["VALUE"], color='b')
    axs[i].set_title(f"Traveller characteristics vs Number of Travellers in {geo}")
    axs[i].set_ylabel("Number of Travellers")
    axs[i].set_xticks(list(char_to_num.values()))
    axs[i].set_xlabel("Traveller characteristics (Numbered)")
    axs[i].set_xticklabels(list(char_to_num.values()))
    axs[i].legend([geo], loc='upper right')



plt.savefig(f"{output_dir}/combined_histograms.png")
