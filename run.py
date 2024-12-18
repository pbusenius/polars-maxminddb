import polars as pl
from polars_maxminddb import ip_lookup_city, ip_lookup_country, ip_lookup_asn, ip_lookup_latitude, ip_lookup_longitude

# Example DataFrame with IP addresses
df = pl.DataFrame(
    {
        "ip_addresses": [
            "92.200.50.6",
            "195.90.212.198",
            "95.173.223.186",
            "121.37.156.226",
        ],
    }
)


# Perform city lookup
df = df.with_columns(
    ip_lookup_city(df["ip_addresses"], "GeoLite2-City.mmdb").alias("city")
)

# Perform country lookup
df = df.with_columns(
    ip_lookup_country(df["ip_addresses"], "GeoLite2-City.mmdb").alias("country")
)

# Perform ASN lookup
df = df.with_columns(
    ip_lookup_asn(df["ip_addresses"], "GeoLite2-ASN.mmdb").alias("asn_name")
)

df = df.with_columns(
    ip_lookup_latitude(df["ip_addresses"], "GeoLite2-City.mmdb").alias("latitude"),
    ip_lookup_longitude(df["ip_addresses"], "GeoLite2-City.mmdb").alias("longitude")
)

print(df)
