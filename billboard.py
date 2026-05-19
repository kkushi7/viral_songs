import billboard
import pandas as pd

songs = []

# pull charts for multiple weeks
chart = billboard.ChartData('hot-100')

# layout of entries for list
for entry in chart:
    songs.append({
        "song": entry.title,
        "artist": entry.artist,
        "rank": entry.rank
    })

df_billboard = pd.DataFrame(songs)

print(df_billboard.head())

df_billboard.to_csv("billboard_hits.csv", index=False)
