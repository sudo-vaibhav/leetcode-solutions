/* Write your PL/SQL query statement below */
with temp as 
(select Visits.visit_id, Transactions.transaction_id from Visits left join
Transactions on Visits.visit_id = Transactions.visit_id),
nulledTemp as (select * from temp where temp.transaction_id is null)
select customer_id,count(*) as count_no_trans from Visits inner join nulledTemp on nulledTemp.visit_id=Visits.visit_id group by customer_id order by count(*) desc;