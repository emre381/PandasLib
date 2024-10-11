import pandas as pd
# s = pd.Series([10,20,30,40], index=["a","b","c","d"])
# print(s)


data = {
    'Price':[45,85,45,25],
    'Number of sales':[5,6,7,2],
    'Category':['Novel','Science','kids','History']
}
df=pd.DataFrame(data)
# print(df)
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df[['Price','Category']])
# filt=df[df['Price']>50]
# print(filt)

df['Total Price'] = df['Price'] * df['Number of sales']  
# print(df)

# df = df.drop('Category',axis=1)
# df['Category'] = ['Novel','Science','kids','History']
print(df)