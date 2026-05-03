"""NextCure Intelligence System - Iteration 1/2 prototype.

Run with:
    streamlit run app.py
"""

from __future__ import annotations

import time

import streamlit as st

from engines.prototype_runner import run_prototype_analysis
from ui.charts import peer_bar_chart, relative_performance_chart, technical_stock_chart
from ui.layout import render_hero, render_insights, render_kpi_cards
from ui.styles import inject_global_styles

st.set_page_config(
    page_title="NextCure Intelligence System",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_styles()

if "analysis_started" not in st.session_state:
    st.session_state.analysis_started = False
if "results" not in st.session_state:
    st.session_state.results = None
if "selected_technical_ticker" not in st.session_state:
    st.session_state.selected_technical_ticker = "NXTC"

render_hero()
st.write("")

left, right = st.columns([0.62, 0.38], gap="large")
with left:
    st.markdown(
        """
        <div class="card">
            <div class="section-title" style="margin-top:0;">One-button operating model</div>
            <div class="muted">
                No tuning panel, no analyst-style clutter. Michael opens the dashboard, presses START ANALYSIS,
                and receives a polished market-positioning readout built from backend defaults.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    if st.button("START ANALYSIS", type="primary"):
        st.session_state.analysis_started = True
        progress = st.progress(0, text="Initializing market positioning layer...")
        steps = [
            "Comparing NXTC to XBI and QQQ...",
            "Constructing peer landscape...",
            "Calculating relative performance...",
            "Building six-month technical charts...",
            "Applying RSI and MACD overlays...",
            "Generating executive readout...",
        ]
        for idx, step in enumerate(steps, start=1):
            time.sleep(0.22)
            progress.progress(idx / len(steps), text=step)
        st.session_state.results = run_prototype_analysis()
        progress.empty()
        st.rerun()

if st.session_state.analysis_started and st.session_state.results is not None:
    results = st.session_state.results
    st.write("")
    render_kpi_cards(results.kpis)
    st.write("")

    overview, technicals, peers, rhythm = st.tabs([
        "Executive Summary",
        "Stock Technicals",
        "Peer Landscape",
        "Market Rhythm",
    ])

    with overview:
        render_insights(results.insights)
        st.plotly_chart(relative_performance_chart(results.performance), use_container_width=True)

    with technicals:
        st.markdown('<div class="section-title">Six-Month Stock Technicals</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="muted" style="margin-bottom: .85rem;">
                CEO-facing technical view: actual price structure first, then RSI and MACD underneath. These are not exposed as system toggles;
                the backend decides the standard six-month lookback and indicator stack.
            </div>
            """,
            unsafe_allow_html=True,
        )
        tickers = list(results.technicals.keys())
        cols = st.columns(len(tickers))
        for col, ticker in zip(cols, tickers):
            df = results.technicals[ticker]
            latest_close = df["Close"].iloc[-1]
            latest_rsi = df["RSI14"].iloc[-1]
            with col:
                if st.button(f"{ticker}", key=f"ticker_{ticker}"):
                    st.session_state.selected_technical_ticker = ticker
                st.markdown(
                    f"""
                    <div class="ticker-card">
                        <div class="ticker-symbol">{ticker}</div>
                        <div class="ticker-read">Close {latest_close:.2f} · RSI {latest_rsi:.0f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        selected = st.session_state.selected_technical_ticker
        st.plotly_chart(technical_stock_chart(results.technicals[selected], selected), use_container_width=True)

    with peers:
        st.markdown('<div class="section-title">Peer Momentum Map</div>', unsafe_allow_html=True)
        st.plotly_chart(peer_bar_chart(results.peer_table), use_container_width=True)
        st.dataframe(results.peer_table, use_container_width=True, hide_index=True)

    with rhythm:
        st.markdown('<div class="section-title">Early Time-Cycle Overlay</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="card">
                <div class="muted">
                    Prototype placeholder: this section will show recurring biotech momentum windows, catalyst-adjacent
                    performance rhythm, and capital-market timing context. In Iteration 3/4, this will be fed by real
                    price history and event windows rather than mock commentary.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.write("")
    st.markdown(
        """
        <div class="card">
            <div class="section-title" style="margin-top:0;">What this prototype demonstrates</div>
            <div class="muted">
                Iteration 1/2 focuses on the product experience first: premium shell, clean START workflow,
                modular architecture, mock intelligence outputs, and a dashboard design that can later be wired to
                real market data without changing the executive-facing interaction model.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
