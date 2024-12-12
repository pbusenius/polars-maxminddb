# Polars MaxMindDB Lookup Plugin

This plugin extends the functionality of [Polars](https://www.pola.rs) by providing methods to look up IP address information using MaxMind databases. It supports city, country, and ASN lookups.

## Features

- **City Lookup:** Retrieves city-level information for a given IP address as a string.
- **Country Lookup:** Retrieves country-level information for a given IP address as a string.
- **ASN Lookup:** Retrieves ASN (Autonomous System Number) name for a given IP address as a string.
- **Integration with Polars:** Works seamlessly with Polars DataFrames, offering fast processing.

## Requirements

- Python 3.8+
- Polars library

Install Polars with:

```bash
uv add polars
```

- MaxMindDB: Download and use the GeoIP2 databases provided by MaxMind (e.g., GeoLite2-City.mmdb, GeoLite2-Country.mmdb, GeoLite2-ASN.mmdb). See [MaxMind](https://www.maxmind.com) for more details.


## Installation

Add the plugin to your project. Install it directly from the repository or manually include the Python file.

```bash
uv add polars-maxminddb
```

## Usage

### Example Code

```python
import polars as pl
from polars_maxminddb import ip_lookup_city, ip_lookup_country, ip_lookup_asn

# Example DataFrame with IP addresses
df = pl.DataFrame({
    "ip_addresses": ["92.200.50.6", "195.90.212.198", "95.173.223.186", "121.37.156.226"],
})


# Perform city lookup
df = df.with_columns(
    ip_lookup_city(df["ip_addresses"]).alias("city")
)

# Perform country lookup
df = df.with_columns(
    ip_lookup_country(df["ip_addresses"]).alias("country")
)

# Perform ASN lookup
df = df.with_columns(
    ip_lookup_asn(df["ip_addresses"]).alias("asn_name")
)

print(df)
```

### Output

The output will include the city, country, and ASN name information as strings. For example:

```
shape: (4, 4)
┌────────────────┬───────────────────┬─────────┬─────────────────────────────────┐
│ ip             ┆ city              ┆ country ┆ asn_name                        │
│ ---            ┆ ---               ┆ ---     ┆ ---                             │
│ str            ┆ str               ┆ str     ┆ str                             │
╞════════════════╪═══════════════════╪═════════╪═════════════════════════════════╡
│ 92.200.50.6    ┆ Sundern           ┆ Germany ┆ Plusnet GmbH                    │
│ 195.90.212.198 ┆ Frankfurt am Main ┆ Germany ┆ EVANZO e-commerce GmbH          │
│ 95.173.223.186 ┆ Lima              ┆ Peru    ┆ Datacamp Limited                │
│ 121.37.156.226 ┆                   ┆ China   ┆ Huawei Cloud Service data cent… │
└────────────────┴───────────────────┴─────────┴─────────────────────────────────┘

```


