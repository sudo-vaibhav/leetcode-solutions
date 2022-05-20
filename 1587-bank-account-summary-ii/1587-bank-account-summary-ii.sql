# Write your MySQL query statement below

select name,sum(Transactions.amount) as balance 
from Users 
inner join
Transactions on Users.account=Transactions.account 
group by Transactions.account having balance>10000