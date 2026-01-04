with p_code as (
    select substring(product_code,1,2) as category, count(*) as products
    from product
    group by  category
)

select * from p_code
order by category

