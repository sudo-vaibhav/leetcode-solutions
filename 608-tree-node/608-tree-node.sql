# Write your MySQL query statement below
# WITH A as (Select id as curID, count(*) as children from Tree having p_id=curID group by curID)
# select * from A
# Tree.id,
# CASE
#     WHEN p_id is NULL then "Root"
#     WHEN A.children=0 then "Leaf"
#     ELSE "Inner"
# END AS type from Tree inner join A on A.id=Tree.id 

select id, case when 
p_id is null then "Root"
when id in (select p_id from Tree) then "Inner"
else "Leaf"
end as Type from Tree