import pandas as pd
import numpy as np

df = pd.DataFrame(columns=['a','b','c'], index=['1','2','3'])
#df.set_index('name',inplace=True)
#df.loc['y'] = pandas.Series({'a':1, 'b':5, 'c':2, 'd':3})
#df.set_index('')

cp = df.loc['1','b']
hej = df.replace(cp, 'X')


#print(hej)
print(hej)