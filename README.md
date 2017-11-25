#   	Test Technque Data Auchan:Direct

#		SQL

_1. Créer une table nommée order_details avec les colonnes suivantes :_

create table order_details(order_id INTEGER, date DATE, nb_products INTEGER, amount DECIMAL(4,2), billed_price DECIMAL(4,2));


_2. Donner le panier moyen par jour. Le panier moyen est le montant moyen par commande sur une période donnée._

	select A.day, AVG(A.final_price) as panier_moyen
	from( 	select o.date as day, o.id, l.product_id,
			sum(l.quantity*(p.price-(p.perc_promo*p.price/100))) as final_price
			from orders o, order_lines l, products p 	
			WHERE o.id = l.order_id
			AND l.product_id = p.id
			GROUP BY o.id, o.date) A
	GROUP BY A.day;


_3. Donner les 5 produits en promos les moins achetés._

select p.id, sum(l.quantity)
from products p, order_lines l
where p.perc_promo != 0
AND p.id = l.product_id
group by p.id
order by sum(l.quantity) ASC
limit 5

# 	Pandas

_Pour lancer le project_

cd pandas
docker build -t pandas .
docker run pandas



Coquilles : products_id est en fait ID
