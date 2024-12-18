import polars as pl
from polars_maxminddb import ip_lookup_city
from polars_maxminddb import ip_lookup_country
from polars_maxminddb import ip_lookup_asn


def test_city():
    df = pl.DataFrame(
        {
            "ip": ["92.200.50.6", "195.90.212.198", "95.173.223.186", "121.37.156.226"],
        }
    )
    result = df.with_columns(city=ip_lookup_city("ip"))

    expected_df = pl.DataFrame(
        {
            "ip": ["92.200.50.6", "195.90.212.198", "95.173.223.186", "121.37.156.226"],
            "city": ["Sundern", "Frankfurt am Main", "Lima", ""],
        }
    )

    assert result.equals(expected_df)


def test_country():
    df = pl.DataFrame(
        {
            "ip": ["92.200.50.6", "195.90.212.198", "95.173.223.186", "121.37.156.226"],
        }
    )
    result = df.with_columns(country=ip_lookup_country("ip"))

    expected_df = pl.DataFrame(
        {
            "ip": ["92.200.50.6", "195.90.212.198", "95.173.223.186", "121.37.156.226"],
            "country": ["Germany", "Germany", "Peru", "China"],
        }
    )

    assert result.equals(expected_df)


def test_asn():
    df = pl.DataFrame(
        {
            "ip": ["92.200.50.6", "195.90.212.198", "95.173.223.186", "121.37.156.226"],
        }
    )
    result = df.with_columns(asn=ip_lookup_asn("ip"))

    expected_df = pl.DataFrame(
        {
            "ip": ["92.200.50.6", "195.90.212.198", "95.173.223.186", "121.37.156.226"],
            "asn": [
                "Plusnet GmbH",
                "EVANZO e-commerce GmbH",
                "Datacamp Limited",
                "Huawei Cloud Service data center",
            ],
        }
    )

    assert result.equals(expected_df)
