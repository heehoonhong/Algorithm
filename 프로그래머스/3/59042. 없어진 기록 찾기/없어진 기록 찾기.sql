SELECT ao.animal_id, ao.name
FROM animal_outs AS ao
WHERE NOT EXISTS (
    SELECT 1
    FROM animal_ins AS ai
    WHERE ao.animal_id = ai.animal_id
)
