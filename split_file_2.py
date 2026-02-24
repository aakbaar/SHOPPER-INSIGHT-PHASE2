import pandas as pd
import numpy as np

# Baca file besar
df = pd.read_csv("AFFINITY_BRAND_CAT_PHASE2.csv")

# Bagi jadi 3 bagian (atau 4 kalau masih terlalu besar)
chunks = np.array_split(df, 2)

for i, chunk in enumerate(chunks):
    chunk.to_csv(f"AFFINITY_BRAND_CAT_PHASE2_part{i}.csv", index=False)

print("Selesai split!")