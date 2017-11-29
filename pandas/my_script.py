import pandas as pd
import matplotlib.pyplot as plt


orders = pd.read_csv("data/orders.csv", names = ["id", "date"])
products = pd.read_csv("data/products.csv", header=None, names = ["product_id", "price", "perc_promo"])
order_lines = pd.read_csv("data/order_lines.csv", header=None, names = ["order_id", "product_id", "quantity"])

#Question 1.1 :





#Question 1.2 : Panier moyen par jour :

PanierMoyen = pd.merge(orders, order_lines, left_on = 'id', right_on = 'order_id')
PanierMoyen = pd.merge(PanierMoyen, products, left_on='product_id', right_on='product_id')

PanierMoyen['final_price'] = PanierMoyen.apply(lambda row: row.quantity * (row.price - (row.perc_promo*row.price/100)), axis = 1)
PanierMoyen = PanierMoyen.groupby(['date', 'id'], as_index=False)['final_price'].sum()
PanierMoyen = PanierMoyen.groupby(['date'], as_index=False)['final_price'].mean()

print("\nPanier moyen par jour :\n")
print(PanierMoyen)

#Question 1.3 :

LessSoldItems = pd.merge(order_lines, products, left_on="product_id", right_on = "product_id")
LessSoldItems = LessSoldItems[(LessSoldItems.perc_promo != 0)]
LessSoldItems = LessSoldItems.groupby(['product_id'], as_index=False)['quantity'].sum()
LessSoldItems = LessSoldItems.sort_values(['quantity', 'product_id'], ascending=True)
print("\n\nLes 5  produits avec reduction les moins achetes :\n")
print(LessSoldItems['product_id'].head(5))
print('\n')


#Question 2 :

QtyPerMonth = pd.merge(orders, order_lines, left_on="id", right_on="order_id")
QtyPerMonth['month'] = pd.to_datetime(QtyPerMonth['date']).dt.month
QtyPerMonth = QtyPerMonth.groupby(['month'], as_index=False)['quantity'].sum()
print(QtyPerMonth)
