-- I'm not even sure what glam rock is
-- rock with bedazzling
SELECT band_name, IFNULL(split, 2020) - formed as lifespan
FROM metal_bands WHERE style LIKE "%Glam rock%";
