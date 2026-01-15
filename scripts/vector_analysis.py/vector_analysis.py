import geopandas as gpd

# Load vector data
gdf = gpd.read_file("data/input/municipalities.shp")

# Reproject to metric CRS
gdf = gdf.to_crs(epsg=31983)

# Create buffer (1 km)
gdf["geometry"] = gdf.geometry.buffer(1000)

# Calculate area in km²
gdf["area_km2"] = gdf.geometry.area / 1_000_000

# Save result
gdf.to_file("data/output/municipalities_buffer.shp")

print("Vector analysis completed successfully.")
