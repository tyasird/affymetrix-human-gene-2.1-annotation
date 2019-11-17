import pandas as pd
import sys
import re

data = pd.read_excel (r'C:/Users/yd/Desktop/input.xlsx') 
df = pd.DataFrame(data)
df["C"] = ""

i=0
for d in df['gene_assignment']:

    result = re.search("^(.*?) \/\/ (.*?) \/\/ (.*?)$",d)
    gene_name = result[2]
    df.loc[i,"C"] = gene_name
    i += 1

df.to_excel("C:/Users/yd/Desktop/output.xlsx") 
