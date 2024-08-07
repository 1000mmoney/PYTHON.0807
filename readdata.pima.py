import pandas as pd
import matplotlib.pyplot as plt

cul_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=cul_names)



print(data.describe().to_csv(./resu/describe.csv))