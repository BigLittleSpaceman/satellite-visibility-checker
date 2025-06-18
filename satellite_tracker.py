from datetime import datetime
import argparse
from pathlib import Path

from skyfield.api import EarthSatellite, load, wgs84
import folium


def load_satellite(tle_path: str) -> EarthSatellite:
    """Load a satellite from a TLE file."""
    with open(tle_path) as f:
        lines = [line.strip() for line in f.readlines()]
    if len(lines) < 3:
        raise ValueError("TLE file must contain at least three lines")
    return EarthSatellite(lines[1], lines[2], lines[0])


def current_position(sat: EarthSatellite):
    """Return the current latitude and longitude of the satellite."""
    ts = load.timescale()
    t = ts.now()
    geocentric = sat.at(t)
    subpoint = wgs84.subpoint(geocentric)
    return subpoint.latitude.degrees, subpoint.longitude.degrees


def create_map(lat: float, lon: float, name: str, output: Path):
    """Create an HTML map showing the satellite location."""
    m = folium.Map(location=[lat, lon], zoom_start=4)
    folium.Marker([lat, lon], popup=name).add_to(m)
    m.save(str(output))


def main():
    parser = argparse.ArgumentParser(
        description="Track a satellite's current position and output a map")
    parser.add_argument(
        "--tle",
        default="data/iss.tle",
        help="Path to a TLE file containing the satellite data",
    )
    parser.add_argument(
        "--output",
        default="satellite_map.html",
        help="Path to the output HTML file",
    )
    args = parser.parse_args()

    satellite = load_satellite(args.tle)
    lat, lon = current_position(satellite)
    create_map(lat, lon, satellite.name, Path(args.output))
    print(f"Map saved to {args.output}")


if __name__ == "__main__":
    main()
