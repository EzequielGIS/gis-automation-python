import geopandas as gpd

areas = gpd.read_file("data/input/municipalities.shp")
landuse = gpd.read_file("data/input/land_use.shp")

landuse = landuse.to_crs(areas.crs)

result = gpd.sjoin(landuse, areas, predicate="intersects")

result.to_file("data/output/landuse_by_municipality.shp")

print("Spatial join completed.")
