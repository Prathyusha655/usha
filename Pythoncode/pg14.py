import pandas as pd
data=pd.read_excel(r'C:\Pythoncode\Companies.xlsx')
df = pd.DataFrame(data, columns=['CEO'])
print(df)

