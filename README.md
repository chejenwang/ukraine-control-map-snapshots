# ukraine-control-map-snapshots


如何記錄這個地圖的變化？我希望能把每天變化的KML資料存起來，每日比較 
https://www.google.com/maps/d/u/1/viewer?hl=en&ll=44.54567297119567%2C30.68157474580051&z=4&mid=1thW9kqnDOaS2lAepLhLdzSX8Ur9Sc4k

<NetworkLink> URL是![CDATA[https://www.google.com/maps/d/u/1/kml?forcekml=1&mid=1thW9kqnDOaS2lAepLhLdzSX8Ur9Sc4k]] ?? <NetworkLink> <name>Russian invasion of Ukraine Control Map</name> <Link> <href><![CDATA[https://www.google.com/maps/d/u/1/kml?forcekml=1&mid=1thW9kqnDOaS2lAepLhLdzSX8Ur9Sc4k]]></href> </Link>

這個 URL 就是「真正的資料出口」

# Ukraine Control Map Time-Series Tracker

This repository tracks day-to-day territorial control changes using
Google My Maps (NetworkLink KML) snapshots.

## Pipeline
1. Fetch daily KML snapshot
2. Normalize geometries (Polygon / MultiPolygon)
3. Compute spatial diffs (gained / lost)
4. Quantify changes (km²)
5. Append to time-series metrics

## Data Source
Google My Maps NetworkLink (KML):
- Russian invasion of Ukraine Control Map

## Requirements
- Python 3.10+
- GDAL-compatible environment

## Usage
```bash
pip install -r requirements.txt
python run_daily.py
