import pandas as pd
from matplotlib import pyplot as plt
from pathlib import Path

path = Path('../../data/ridership_data.csv')
df = pd.read_csv(path, parse_dates=['service_date'], thousands=',')
df.columns = ["date", "day_type", "bus", "rail", "total"]
df = df.sort_values("date").set_index("date")
df = df.drop("total", axis=1)
df = df.drop_duplicates()

diff_7 = df[["bus", "rail"]].diff(7)["2019-03":"2019-05"]

# 아래는 7만큼의 shift를 한 데이터와 원본 데이터가 자기상관성을 보임을 증명한 데이터 시각화이다.
fig, axs = plt.subplots(2, 1, sharex=True, figsize=(8, 5))
df.plot(ax=axs[0], legend=True, marker=".")
df.shift(7).plot(ax=axs[0], grid=True, legend=False, linestyle=":")
diff_7.plot(ax=axs[1], grid=True, marker=".")
plt.show()

# MAE 계산
# abs()는 각 원소를 절댓값으로 바꾸고, mean()은 DataFrame의 각 열별 평균을 계산한다.
# plt.show()는 블로킹 동작이라서 그래프를 닫으면 결과 출력
mae = diff_7.abs().mean()
print(f"MAE: bus={mae['bus']}, rail={mae['rail']}")
# MAPE 계산
# 원본 타겟값과의 비교
targets = df[["bus", "rail"]]["2019-03":"2019-05"]
mape = (diff_7 / targets).abs().mean()
print(f"MAPE: bus={mape['bus']}, rail={mape['rail']}")
