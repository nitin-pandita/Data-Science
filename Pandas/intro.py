# Introduction to Pandas

#import 
import pandas as pd

iris = pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')

# print(type(iris))


df = iris.copy()

print(df.head())


# df.shape
# df.dtypes

# print(df.columns)

df.columns = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width','Flower_type']

# print(df.dtypes)
# print(df.describe())

# print(df.sepal.length)

# print(df.isnull())
# print(df.isnull().sum())

print(df.iloc[1:3,2:5])
