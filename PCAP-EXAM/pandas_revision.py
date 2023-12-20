import pandas as pd

fecha = '20231205'
print(type(pd.Timestamp.today().strftime('%Y%m%d')))

print(fecha >= pd.Timestamp.today().strftime('%Y%m%d'))
