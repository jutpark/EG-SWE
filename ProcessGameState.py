import pandas as pd
from shapely import Polygon
from shapely import Point
# read
df = pd.read_parquet('game_state_frame_data.parquet')

df.to_csv('uwu.csv')

# write
df.to_parquet('my_newfile.parquet')

df.head()

from shapely import Polygon
x=Polygon([[-1735, 250], [-2024, 398], [-2806, 742], [-2472, 1233], [-1565, 580]])

print(len(df.index))
count=0
for index, row in df.iterrows():
    y=Point(row['x'],row['y'])
    if(y.within(x)):
        count+=1
print(count)

