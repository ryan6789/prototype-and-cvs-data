# 수면 관리 프로토타입 (1차 보고서용)

슬라이드에 넣을 이미지: `prototype.png` (16:9)

## 다시 만들기
```
pip install -r requirements.txt
python make_sample_data.py   # 예시 데이터 (10명 x 7일)
python analyze.py            # prototype.png 생성
```
- 실제 데이터가 생기면 `sample_data.csv`를 같은 열 이름(id, 일차, 영상, 소통, 쇼핑, 게임, 수면시간, 피로도)으로 바꾸고 `analyze.py`만 실행.
- 폰트는 Windows 맑은 고딕 기준.
- 이미지의 데이터는 예시이므로 "예시 데이터" 문구를 지우지 말 것.
