from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import polars as pl
from polars.plugins import register_plugin_function

from polars_maxminddb._internal import __version__ as __version__

if TYPE_CHECKING:
    from polars_maxminddb.typing import IntoExprColumn

LIB = Path(__file__).parent


def ip_lookup_city(expr: IntoExprColumn) -> pl.Expr:
    return register_plugin_function(
        args=[expr],
        plugin_path=LIB,
        function_name="ip_lookup_city",
        is_elementwise=True,
    )


def ip_lookup_country(expr: IntoExprColumn) -> pl.Expr:
    return register_plugin_function(
        args=[expr],
        plugin_path=LIB,
        function_name="ip_lookup_country",
        is_elementwise=True,
    )


def ip_lookup_asn(expr: IntoExprColumn) -> pl.Expr:
    return register_plugin_function(
        args=[expr],
        plugin_path=LIB,
        function_name="ip_lookup_asn",
        is_elementwise=True,
    )