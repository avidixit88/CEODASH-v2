"""Reusable layout fragments for the dashboard."""

from __future__ import annotations

import streamlit as st

from config.settings import APP_SUBTITLE, APP_TITLE, APP_VERSION


def render_hero() -> None:
    st.markdown(
        f"""
        <div class="hero">
            <div class="status-pill">● {APP_VERSION}</div>
            <div class="eyebrow" style="margin-top: 1.1rem;">{APP_SUBTITLE}</div>
            <h1>{APP_TITLE}</h1>
            <p>
                A CEO-ready market intelligence surface for understanding whether the market is working for NextCure,
                how NXTC is behaving relative to biotech and Nasdaq benchmarks, and where peer momentum is concentrating.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_kpi_cards(kpis: list[dict[str, str]]) -> None:
    cols = st.columns(len(kpis))
    for col, item in zip(cols, kpis):
        with col:
            st.markdown(
                f"""
                <div class="card">
                    <div class="metric-label">{item['label']}</div>
                    <div class="metric-value">{item['value']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_insights(insights: list[str]) -> None:
    st.markdown('<div class="section-title">Executive Readout</div>', unsafe_allow_html=True)
    for insight in insights:
        st.markdown(f'<div class="insight">{insight}</div>', unsafe_allow_html=True)
