import pandas as pd
data=pd.read_csv(r'C:\Pythoncode\Gaints.csv')
df = pd.DataFrame(data, columns=['CEO', 'Establishment'])
print(df)