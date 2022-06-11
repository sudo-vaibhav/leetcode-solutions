# Write your MySQL query statement below
with redId as (select com_id from Company where name="RED")
# select * from redId
select name from SalesPerson 
where sales_id not in (select sales_id from Orders where com_id in (select com_id from redId)) 