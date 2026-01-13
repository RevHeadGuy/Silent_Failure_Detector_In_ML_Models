import streamlit as st
import plotly.express as px
import pandas as pd

def plot_drift_line_chart(drift_df, metric_name="mean_shift"):
    """
    drift_df: DataFrame with columns ['timestamp', 'mean_shift', 'std_shift', 'distribution_distance']
    """
    fig = px.line(
        drift_df, 
        x="timestamp", 
        y=metric_name, 
        title=f"{metric_name} over time",
        markers=True
    )
    fig.update_layout(
        xaxis_title="Time",
        yaxis_title=metric_name,
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_feature_bar_chart(feature_df):
    """
    feature_df: DataFrame with columns ['feature', 'psi', 'kl', 'severity']
    """
    fig = px.bar(
        feature_df,
        x="feature",
        y="psi",
        color="severity",
        color_discrete_map={
            "NORMAL": "#28a745",
            "LOW": "#ffc107",
            "MEDIUM": "#fd7e14",
            "HIGH": "#dc3545"
        },
        text="psi",
        title="Feature Drift PSI"
    )
    fig.update_layout(
        xaxis_title="Feature",
        yaxis_title="PSI",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)
