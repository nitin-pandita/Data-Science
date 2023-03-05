import pandas as pd

iris = pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')


df = iris



a = df.drop(1) # creating a copy
# print(a.head())

# now if we want to remove it from df itself then

# df.drop(1, inplace= True)
# print(df.head())

# df.drop(1, inplace= True)
# print(df.head())

# print(df.index)

# print(df.head())


# df.drop(df.index[0:3], inplace=True)

# print(df.head())

# print(df.head())


df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width','Flower_type']

# print(df.head())

# print(df.sepal_length > 5)

#boolean condition

# print(df[df.sepal_length > 5])


df.loc[170] = [1,2,3,4,'Kartik']
print(df.tail())



