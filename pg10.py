import pandas as pd
data = {'Country': ['Belgium', 'India', 'Brazil'] ,'Capital': ['Brussels', 'New delhi', 'Brasillia'],'Population': [11111111,22222222,33333333]}
df = pd.DataFrame(data,columns=['Country', 'Capital', 'Population'])
print(df)

