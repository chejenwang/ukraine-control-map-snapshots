import geopandas as gpd
from pathlib import Path

RAW = Path("../data/raw_kml")
OUT = Path("outputs/geojson")
OUT.mkdir(parents=True, exist_ok=True)

for kml in sorted(RAW.glob("*.kml")):
    date = kml.stem
    gdf = gpd.read_file(kml, driver="KML")
    gdf["snapshot_date"] = date
    gdf.to_file(OUT / f"{date}.geojson", driver="GeoJSON")
    print(f"Converted {date}")
