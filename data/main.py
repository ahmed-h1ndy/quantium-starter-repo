import pandas as pd

df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')

# full dataset
df = pd.concat([df1, df2, df3], ignore_index=True)

# print the df length before extracting 'Pink Morsels' and excluding other products
df = df[df['product'] == 'pink morsel']

# remove the '$' from the price, then convert it to a float
df['price'] = df['price'].str.replace('$', '', regex=False)
df['price'] = df['price'].astype(float)

# calculate the sales column
df['sales'] = df['price'] * df['quantity']

# remove redundent columns
df.drop('price', axis = 1, inplace=True)
df.drop('quantity', axis = 1, inplace = True)
df.drop('product', axis = 1, inplace = True)

df.to_csv('daily_sales_data_full.csv')

print(df)


