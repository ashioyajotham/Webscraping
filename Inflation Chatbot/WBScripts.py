import wbgapi as wb
wb.source.info() # looking around

# Accessing data
for row in wb.data.fetch('SP.POP.TOTL', 'USA'): # all years
    print(row)

# Accessing ecomies df
wb.economy.DataFrame()

# Accessing series df
wb.series.DataFrame()
