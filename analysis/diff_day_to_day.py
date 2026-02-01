import geopandas as gpd
from pathlib import Path

GEO = Path("outputs/geojson")
OUT = Path("outputs/diff")
OUT.mkdir(parents=True, exist_ok=True)

files = sorted(GEO.glob("*.geojson"))

for prev, curr in zip(files, files[1:]):
    d1 = gpd.read_file(prev)
    d2 = gpd.read_file(curr)

    date1 = prev.stem
    date2 = curr.stem

    # 新增區域（今天有，昨天沒有）
    new = gpd.overlay(d2, d1, how="difference")

    # 消失區域（昨天有，今天沒有）
    lost = gpd.overlay(d1, d2, how="difference")

    new.to_file(OUT / f"new_{date2}.geojson", driver="GeoJSON")
    lost.to_file(OUT / f"lost_{date2}.geojson", driver="GeoJSON")

    print(f"Diff {date1} → {date2} done")
