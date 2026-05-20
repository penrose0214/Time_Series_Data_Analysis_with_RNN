import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

path = Path('../../data/ridership_data.csv')
df = pd.read_csv(path, parse_dates=['service_date'], thousands=',')
df.columns = ["date", "day_type", "bus", "rail", "total"]
df = df.sort_values("date").set_index("date")
df = df.drop("total", axis=1)
df = df.drop_duplicates()

origin, today = "2019-01-01", "2019-05-31"
# asfreq("D")는 날짜 인덱스를 일(day) 단위 빈도로 맞춰 시계열의 간격을 명시한다.
rail_series = df.loc[origin:today]["rail"].asfreq("D")
# order는 일반적인 단기 패턴을, seasonal_order는 s=7 기준의 주기적 계절 패턴을 모델링한다.
model = ARIMA(rail_series,
              order=(1, 0, 0),
              seasonal_order=(0, 1, 1, 7))
model = model.fit()
y_pred = model.forecast()
print(y_pred)
