SELECT
    id,
    ST_X(ST_Centroid(ST_Transform(bounds, 4326))) AS longitude,
    ST_Y(ST_Centroid(ST_Transform(bounds, 4326))) AS latitude
FROM japan_segments;
