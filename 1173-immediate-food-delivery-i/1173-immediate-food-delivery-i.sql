# Write your MySQL query statement below
with A as (select count(*) as imm from Delivery where order_date=customer_pref_delivery_date)
select ROUND(100*A.imm/count(*),2) as immediate_percentage from A inner join Delivery