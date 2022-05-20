# Write your MySQL query statement below
select product_id, store1 as price,"store1" as store from Products where  store1 is not null
union
select product_id, store2 as price,"store2" as store from Products where  store2 is not null
union
select product_id, store3 as price,"store3" as store from Products where  store3 is not null

