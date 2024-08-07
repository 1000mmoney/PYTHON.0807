import pandas as pd
import numpy

my_index = ['e', 'w', 's', 'w']
my_columns = ['이름', '나이', '속성']
my_data = numpy.array([['청룡', '백호', '주작', '현무'],
                       [200, 300, 250, 300],
                       ['하늘', '대지', '산', '바다']]).transpose()

df = pd.DataFrame(my_data, index=my_index, columns=my_columns)
print(df, "\n", df.loc["e"])