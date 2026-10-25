# 예시 데이터 생성 (실제 수집 전 임시용): 10명 x 7일
import numpy as np
import pandas as pd

rng = np.random.default_rng(14)
people, days = 10, 7
cols = ["영상", "소통", "쇼핑", "게임"]
mean = np.array([1.4, 0.8, 0.5, 0.9])  # 22~04시 평균 이용시간(시간)

rows = []
for i in range(1, people + 1):
    taste = rng.uniform(0.4, 1.8, 4)  # 사람마다 즐기는 매체가 다름
    for d in range(1, days + 1):
        use = (rng.gamma(2.0, mean * taste / 2.0)).clip(0, 5)
        sleep = 7.6 - 0.42 * use[0] - 0.08 * use[1] - 0.21 * use[2] - 0.55 * use[3] + rng.normal(0, 0.7)
        sleep = float(np.clip(sleep, 3.5, 9.5))
        fatigue = int(np.clip(round(10 - sleep + rng.normal(0, 1.1)), 1, 10))
        rows.append([i, d, *use.round(2), round(sleep, 1), fatigue])

df = pd.DataFrame(rows, columns=["id", "일차", *cols, "수면시간", "피로도"])
df.to_csv("sample_data.csv", index=False, encoding="utf-8-sig")
print(df.head())
