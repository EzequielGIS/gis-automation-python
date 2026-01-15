import rasterio
import numpy as np

with rasterio.open("data/input/landsat.tif") as src:
    red = src.read(3).astype(float)
    nir = src.read(4).astype(float)
    profile = src.profile

ndvi = (nir - red) / (nir + red)

profile.update(dtype=rasterio.float32, count=1)

with rasterio.open("data/output/ndvi.tif", "w", **profile) as dst:
    dst.write(ndvi.astype(rasterio.float32), 1)

print("NDVI generated successfully.")
