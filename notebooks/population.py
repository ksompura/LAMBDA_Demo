import matplotlib.pyplot as plt
import pandas
import random

df = pandas.read_csv('../data/atlantis.csv')
x = df['year']
y = df['population']

plt.plot(x,y)
plt.title("Population of Atlantis")
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()
print('Wow thats a steep decline')