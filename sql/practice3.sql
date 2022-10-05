SELECT id
FROM japan_segments
WHERE ST_Contains(ST_GeomFromGeoJSON('{
    "type": "Polygon",
    "coordinates": [
      [
        [
          130.27313232421875,
          30.519681272749402
        ],
        [
          131.02020263671875,
          30.519681272749402
        ],
        [
          131.02020263671875,
          30.80909017893796
        ],
        [
          130.27313232421875,
          30.80909017893796
        ],
        [
          130.27313232421875,
          30.519681272749402
        ]
      ]
    ]}')::geography::geometry, bounds);
