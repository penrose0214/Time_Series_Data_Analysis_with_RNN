import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

path = Path('../../data/ridership_data.csv')
df = pd.read_csv(path, parse_dates=['service_date'], thousands=',')
df.columns = ["date", "day_type", "bus", "rail", "total"]
df = df.sort_values("date").set_index("date")
df = df.drop("total", axis=1)
df = df.drop_duplicates()

fig, ax = plt.subplots(figsize=(8, 3.5))
df["2019-03":"2019-05"].plot(ax=ax, grid=True, marker=".")
plt.show()
