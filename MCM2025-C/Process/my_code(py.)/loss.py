"""
xiangchuyang needed.

Little gadget calculating loss.
2016

"""

import pandas as pd

ref_2016_total = {
    "NOC": ["USA", "GBR", "CHN", "RUS", "GER", "JPN", "FRA", "KOR", "ITA", "AUS", "NED", "HUN", "BRA", "ESP", "KEN"],
    "Gold0": [46, 27, 26, 19, 17, 12, 10, 9, 8, 8, 8, 8, 7, 7, 6],
    "Silver0": [37, 23, 18, 17, 10, 8, 18, 3, 12, 11, 7, 3, 6, 4, 6],
    "Bronze0": [38, 17, 26, 20, 15, 21, 14, 9, 8, 10, 4, 4, 6, 6, 1]
}

ref_2016_old_athlete = {
    "NOC": ["USA", "GBR", "RUS", "CHN", "GER", "ARG", "SRB", "BRA", "FRA", "JPN", "SUI", "DEN", "CRO", "NZL", "HUN"],
    "Gold0": [44, 38, 20, 16, 13, 13, 9, 9, 8, 6, 6, 5, 5, 5, 5],
    "Silver0": [12, 15, 7, 7, 9, 0, 6, 1, 22, 5, 1, 7, 7, 5, 0],
    "Bronze0": [24, 10, 13, 13, 20, 0, 1, 3, 10, 17, 2, 7, 0, 2, 2]
}

reference_data = ref_2016_old_athlete

reference_df = pd.DataFrame(reference_data)
input_df = pd.read_csv(r"C:\Users\weiyi\Desktop\1_4_01_aggregated_by_noc(1).csv")
total_sum = 0

for _, ref_row in reference_df.iterrows():
    noc = ref_row["NOC"]
    gold0 = ref_row["Gold0"]
    silver0 = ref_row["Silver0"]
    bronze0 = ref_row["Bronze0"]
    
    input_row = input_df[input_df["NOC"] == noc]
    
    if not input_row.empty:
        gold = input_row["Gold"].values[0]
        silver = input_row["Silver"].values[0]
        bronze = input_row["Bronze"].values[0]
        
        weighted_diff = (
            0.6 * (gold0 - gold) ** 2 +
            0.3 * (silver0 - silver) ** 2 +
            0.1 * (bronze0 - bronze) ** 2
        )
        
        total_sum += weighted_diff

print(f"Total Sum: {total_sum}")