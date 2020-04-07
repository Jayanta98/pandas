# cook your dish here
import pandas as pd
import numpy as np
df=pd.DataFrame({'col1':[102,131,242,159,753],
                 'col2':[652,125,962,742,632],
                 'col3':[654,852,651,245,476],
                 'col4':[251,644,855,215,488]})
print(df)
gh=df.reset_index().replace({'index': {0:1}}).groupby('index',sort=False).sum() 
print(gh)
gh.reset_index(inplace=True)
print(gh)