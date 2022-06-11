# Write your MySQL query statement below


with A as (select customer_id,Product.product_id,sum(price*quantity) as tot from (Orders 
inner join
Product on Product.product_id=Orders.product_id) where EXTRACT(year from order_date)=2020 and EXTRACT(month from order_date)=6 group by customer_id having tot>=100),
B as
(select customer_id,Product.product_id,sum(price*quantity) as tot from (Orders 
inner join
Product on Product.product_id=Orders.product_id) where EXTRACT(year from order_date)=2020 and EXTRACT(month from order_date)=7 group by customer_id having tot>=100),
C as (
select A.customer_id as customer_id from
A
inner join
B
on A.customer_id=B.customer_id
)
select C.customer_id, name from Customers 
inner join 
C on
C.customer_id=Customers.customer_id