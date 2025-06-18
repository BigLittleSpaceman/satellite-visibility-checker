# satellite-visibility-checker

A simple prototype for tracking satellites and displaying their current location on a map.

## Requirements

- Python 3.8+
- [skyfield](https://rhodesmill.org/skyfield/)
- [folium](https://python-visualization.github.io/folium/)

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the tracker to generate an HTML map of the satellite position:

```bash
python satellite_tracker.py --tle data/iss.tle --output satellite_map.html
```

Open the generated `satellite_map.html` in your browser to see the marker of the satellite's current subpoint on Earth.

The repository ships with a sample TLE for the ISS in `data/iss.tle`. You can replace this file with updated TLE data or supply your own via the `--tle` argument.
