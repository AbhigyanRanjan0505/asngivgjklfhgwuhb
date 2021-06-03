import pandas as pd

df = pd.read_csv("data.csv")
df.head()

bools_distance = []
for distance in df.Distance:
    if distance <= 100:
        bools_distance.append(True)
    else:
        bools_distance.append(False)

temp_distance = pd.Series(bools_distance)
temp_distance.head()

distance = df[temp_distance]

distance.reset_index(inplace=True, drop=True)
distance.head()

bools_gravity = []
for gravity in df.Gravity:
    if gravity <= 350 and gravity >= 150:
        bools_gravity.append(True)
    else:
        bools_gravity.append(False)

gravity_support = pd.Series(bools_gravity)
gravity_support.head()

final_stars = df[gravity_support]
final_stars.head()

final_stars.shape
final_stars.reset_index(inplace=True, drop=True)
final_stars.head()

final_stars.to_csv("final_data.csv")
