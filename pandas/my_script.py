import pandas as pd

orders = pd.read_csv("data/orders.csv", names = ["id", "date"])
products = pd.read_csv("data/products.csv", header=None, names = ["product_id", "price", "perc_promo"])
order_lines = pd.read_csv("data/order_lines.csv", header=None, names = ["order_id", "product_id", "quantity"])

#Question 1 :





#Question 2 : Panier moyen par jour :

mergedDF = pd.merge(orders, order_lines, left_on = 'id', right_on = 'order_id')
mergedDF = pd.merge(mergedDF, products, left_on='product_id', right_on='product_id')

mergedDF['final_price'] = mergedDF.apply(lambda row: row.quantity * (row.price - (row.perc_promo*row.price/100)), axis = 1)
DF = mergedDF.groupby(['date', 'id'], as_index=False)['final_price'].sum()
PanierMoyen = DF.groupby(['date'], as_index=False)['final_price'].mean()

print("Panier moyen par jour : ")
print(PanierMoyen)
