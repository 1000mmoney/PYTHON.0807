import pandas as pd

data = {'이름': ['청룡', '백호', '주작', '현무'],
        '나이': [200, 300, 250, 400],
        '속성': ['물', '바람', '불', '바다'], }

df = pd.DataFrame(data, index=['E', 'W', 'S', 'N'])
print(df)
# df.to_csv("./data.scv")