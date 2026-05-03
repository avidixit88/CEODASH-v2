"""Prototype orchestration layer for Iteration 1/2.

The app calls this single runner when START ANALYSIS is pressed. Later, this
becomes the orchestration point for real market data, peer logic, technical
analysis, and insight engines without changing the UI contract.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from data.mock_market_data import (
    build_mock_insights,
    build_mock_kpi_cards,
    build_mock_peer_table,
    build_mock_performance,
    build_mock_technical_data,
)


@dataclass(frozen=True)
class PrototypeResults:
    performance: pd.DataFrame
    peer_table: pd.DataFrame
    technicals: dict[str, pd.DataFrame]
    kpis: list[dict[str, str]]
    insights: list[str]


def run_prototype_analysis() -> PrototypeResults:
    return PrototypeResults(
        performance=build_mock_performance(),
        peer_table=build_mock_peer_table(),
        technicals=build_mock_technical_data(),
        kpis=build_mock_kpi_cards(),
        insights=build_mock_insights(),
    )
