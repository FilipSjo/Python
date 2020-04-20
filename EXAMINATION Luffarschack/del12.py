import pandas as pd
import numpy as np

df = pd.DataFrame(columns=['a','b','c'], index=['1','2','3'])
#df.set_index('name',inplace=True)
#df.loc['y'] = pandas.Series({'a':1, 'b':5, 'c':2, 'd':3})
#df.set_index('')
df['a'].replace(['ABC', 'AB'], 'A')
hej2 = df.loc['1','b']
hej = df.replace(hej2, 'X')

#dict med unik key(exempelvis en siffra, sedan sparas 'X', 'O' som value och swappas?)
#print(hej)
print(hej)