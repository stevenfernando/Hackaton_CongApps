import pandas as pd 

arch= "informacion.txt"
df2 = pd.read_csv(arch, delimiter='\t')

column_names = list(df2.columns.values)

print(column_names)