import pandas as pd
import os

df = pd.read_csv("offshore_windspeeds_NVE_areas.csv")


print(df.head())


print(df["locID"])

print("Unique locIDs:", df["locID"].unique())

# Separate data fra 1 til 20
output_folder = "split_data"
os.makedirs(output_folder, exist_ok=True)

# Check unique locIDs
unique_ids = sorted(df["locID"].unique())
print("Unique locIDs found:", unique_ids)

# separate data for each locID and save to CSV
for loc_id in unique_ids:
    subset = df[df["locID"] == loc_id]
    
    
    subset.to_csv(f"data_locID_{loc_id}.csv", index=False)
    print(f"Saved data for locID {loc_id} with {len(subset)} rows.")
print("\nAll locID files have been successfully created!")

