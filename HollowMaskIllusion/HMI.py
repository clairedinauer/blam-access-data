import pandas as pd
from collections import Counter

df_HMI = pd.read_excel('HollowMaskExcel.xlsx', sheet_name='HMI_Simplified')


print(dict(Counter(df_HMI.T012)))
