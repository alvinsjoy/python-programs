import pandas as pd
import matplotlib.pyplot as plt

a = pd.Series([1, 2, 3, 4, 5], index =['one', 'two', 'three', 'four', 'five'])
print(a)

d = {
    'a': 'apple',
    'b': 'ball',
    'c': 'cat',
    'd': 'dog'
}
ds = pd.Series(d)
print(ds)

# usage of head
print(ds.head(2))
print(ds.tail(2))

x = ['random', 'set', 'of', 'words', 'to', 'test', 'the', 'pandas', 'library', 'and', 'its', 'functionality']
y = pd.DataFrame(x)
print(y)

x = {
    'name': ['John', 'Jane', 'Doe', 'Smith', 'Emily', 'Sarah', 'Eva'],
    'age': [28, 34, 29, 40, 22, 35, 30],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio']
}
df = pd.DataFrame(x)
print(df)

print(df.iloc[1])

print('Size: ', df.size)
print('Shape: ', df.shape)

print(df.values)
print(df.describe())
print(df['age'])
plt.bar(df['name'], df['age'])
plt.show()

df.to_csv('data.csv')
df = pd.read_csv('data.csv')
print(df)
