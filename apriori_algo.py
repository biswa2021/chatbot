import pandas as pd
import os
data=pd.read_excel(
     os.path.join('/Users/biswaranjantripathy/Desktop/myproject/retail.xlsx'),engine='openpyxl')
#data1=data.head(1000)

data1=data[data['Quantity']>0].head(1000)
print(data1)

data1.columns
data1.Country.unique()
data1['Description']=data1['Description'].str.strip()
data1.dropna(axis=0,subset=['InvoiceNo'],inplace=True)

basket_UK = (data1[data1['Country'] =="United Kingdom"] 
          .groupby(['InvoiceNo', 'Description'])['Quantity'] 
          .sum().unstack().reset_index().fillna(0) 
          .set_index('InvoiceNo'))

basket_UK.head(10).to_csv('/Users/biswaranjantripathy/Desktop/myproject/sample.csv')

def hot_encode(x):
    if x<=0:
        return 0
    if x>=1:
        return 1
basket_en=basket_UK.applymap(hot_encode)
basket_UKE=basket_en
basket_UKE

from mlxtend.frequent_patterns import apriori,association_rules
frq_itms=apriori(basket_UKE,min_support=0.05,use_colnames=True)

rule=association_rules(frq_itms,metric='lift',min_threshold=1)
rule=rule.sort_values(['confidence','lift'])
rule
