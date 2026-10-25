import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy import stats

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 데이터 불러오기
df = pd.read_csv("sample_data.csv")
media = ["영상", "소통", "쇼핑", "게임"]
color = ["#2563EB", "#16A34A", "#D97706", "#DC2626"]

# 매체별 이용 비중
total = df[media].sum()
share = total / total.sum() * 100

# 매체별 이용시간과 수면시간의 상관계수
r = []
p = []
for m in media:
    result = stats.pearsonr(df[m], df["수면시간"])
    r.append(result[0])
    p.append(result[1])

worst = media[r.index(min(r))]
print(dict(zip(media, [round(x, 2) for x in r])), worst)

# 경고문 (23시 이후 60분 초과 기준을 단순화해서 22~04시 이용시간으로 대체)
user = df.loc[df[worst].idxmax()]
minutes = user[worst] * 60
if minutes > 60:
    msg = "현재 " + worst + " 이용이 내일의 피로도를 높이고 있습니다. 이제 화면을 끌 시간입니다."
else:
    msg = "오늘은 위험 기준 이내입니다."

# 그래프
fig = plt.figure(figsize=(14.56, 8.19), dpi=100, facecolor="#F2F2F2")

for box in [(0.05, 0.28, 0.42, 0.53), (0.50, 0.28, 0.45, 0.53), (0.05, 0.07, 0.90, 0.17)]:
    fig.add_artist(FancyBboxPatch(box[:2], box[2], box[3], boxstyle="round,pad=0,rounding_size=0.012",
                                  transform=fig.transFigure, fc="white", ec="#D5DCE8", zorder=-1))

fig.text(0.05, 0.93, "CHAPTER 04. 프로토타입", color="#2563EB", fontsize=12, weight="bold")
fig.text(0.05, 0.865, "야간 미디어 이용 분석 결과 (예시)", color="#111827", fontsize=26, weight="bold")

# 파이 차트
ax1 = fig.add_axes([0.07, 0.30, 0.38, 0.42])
ax1.pie(share, labels=media, colors=color, startangle=90, counterclock=False,
        autopct="%.1f%%", pctdistance=0.72, textprops={"fontsize": 12},
        wedgeprops={"edgecolor": "white", "linewidth": 2})
for t in ax1.texts:
    if t.get_text().endswith("%"):
        t.set_color("white")
fig.text(0.07, 0.75, "4대 매체 야간 이용 비중 (10명 × 7일)", fontsize=15, weight="bold")

# 막대 그래프
ax2 = fig.add_axes([0.55, 0.36, 0.37, 0.34])
bars = ax2.barh(media, r, color=color, height=0.55)
ax2.invert_yaxis()
ax2.axvline(0, color="gray", lw=1)
ax2.set_xlim(-0.8, 0.1)
for s in ["top", "right", "left"]:
    ax2.spines[s].set_visible(False)
ax2.tick_params(length=0, labelsize=12)
for i in range(4):
    label = "r = %.2f" % r[i]
    if p[i] < 0.05:
        label += "*"
    ax2.text(r[i] - 0.02, i, label, va="center", ha="right", fontsize=11)
fig.text(0.52, 0.75, "이용시간과 수면시간의 상관계수", fontsize=15, weight="bold")
fig.text(0.52, 0.30, "* p < 0.05", color="gray", fontsize=10)

# 경고 문구
fig.text(0.07, 0.205, "맞춤형 경고  |  가장 부정적 영향: " + worst, color="#DC2626", fontsize=13, weight="bold")
fig.text(0.07, 0.16, "학생 #%d (%d일차)  ·  22시~04시 %s %d분 (기준 60분)" % (user["id"], user["일차"], worst, minutes),
         color="gray", fontsize=12)
fig.text(0.07, 0.115, '"' + msg + '"', fontsize=15, weight="bold")

fig.text(0.95, 0.025, "※ 예시 데이터 (10명 × 7일, 실제 수집 전)", color="gray", fontsize=10, ha="right")

fig.savefig("prototype.png", facecolor="#F2F2F2")
