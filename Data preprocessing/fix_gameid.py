import pandas as pd

path = '../Data/RAW/FBREF_Dataset/la-liga_2023-2024_fixture_data.csv'
df = pd.read_csv(path)
df['game_id'] = range(len(df))

# print(df)

df.to_csv(path, index=False)