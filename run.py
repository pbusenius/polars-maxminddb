import polars as pl
from polars_maxminddb import ip_lookup_city
from polars_maxminddb import ip_lookup_country
from polars_maxminddb import ip_lookup_asn


df = pl.DataFrame(
    {
        "ip": ["92.200.50.6", "195.90.212.198", "95.173.223.186", "121.37.156.226"],
    }
)

df = df.with_columns(city=ip_lookup_city("ip"))
df = df.with_columns(country=ip_lookup_country("ip"))
df = df.with_columns(asn=ip_lookup_asn("ip"))

print(df)

df.write_csv("out.csv")
