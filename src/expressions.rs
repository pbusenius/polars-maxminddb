#![allow(clippy::unused_unit)]
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;
use std::fmt::Write;
use maxminddb::geoip2;


#[polars_expr(output_type=String)]
fn ip_lookup_city(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;
    let reader = maxminddb::Reader::open_readfile("GeoLite2-City.mmdb").unwrap();

    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        let city_name: &str;
        let ip= value.parse().unwrap();

        let resp: geoip2::City = reader.lookup(ip).unwrap();
        
        match resp.city {
            Some(city) => {
                let names = city.names.unwrap();
                match names.get("en") {
                    Some(name) => city_name = name,
                    None => city_name = ""
                }
            },
            None => city_name = "",
        }

        write!(output, "{}", city_name).unwrap()

    });

    Ok(out.into_series())
}

#[polars_expr(output_type=String)]
fn ip_lookup_country(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;
    let reader = maxminddb::Reader::open_readfile("GeoLite2-City.mmdb").unwrap();

    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        let country_name: &str;
        let ip= value.parse().unwrap();

        let resp: geoip2::City = reader.lookup(ip).unwrap();
        
        match resp.country {
            Some(country) => {
                let names = country.names.unwrap();
                match names.get("en") {
                    Some(name) => country_name = name,
                    None => country_name = ""
                }
            },
            None => country_name = "",
        }

        write!(output, "{}", country_name).unwrap()

    });

    Ok(out.into_series())
}


#[polars_expr(output_type=String)]
fn ip_lookup_asn(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;
    let reader = maxminddb::Reader::open_readfile("GeoLite2-ASN.mmdb").unwrap();

    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        let asn_name: &str;
        let ip= value.parse().unwrap();

        let resp: geoip2::Asn = reader.lookup(ip).unwrap();
        
        match resp.autonomous_system_organization {
            Some(asn) =>         asn_name = asn,
            None => asn_name = "",
        }

        write!(output, "{}", asn_name).unwrap()

    });

    Ok(out.into_series())
}