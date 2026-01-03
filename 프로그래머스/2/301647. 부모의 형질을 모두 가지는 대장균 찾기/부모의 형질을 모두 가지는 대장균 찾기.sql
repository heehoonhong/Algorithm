select edc.id,edc.genotype,edp.genotype as parent_genotype from ecoli_data edc 
join ecoli_data edp
on edc.parent_id=edp.id
where (edc.genotype&edp.genotype)=edp.genotype
order by edc.id asc