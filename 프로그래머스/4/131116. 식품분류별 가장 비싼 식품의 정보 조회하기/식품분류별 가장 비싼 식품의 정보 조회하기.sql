with f as (
    select category, price as max_price, product_name,
    rank() over (partition by category order by price desc ) as rn
    from food_product
    where category in ('과자','국','김치','식용유')
)
select category,max_price,product_name from f
where rn=1
order by max_price desc