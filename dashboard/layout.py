import streamlit as st

def render_title(title):
    st.markdown(f"## {title}")

def render_metric(title, value, severity="healthy"):
    colors = {
        "healthy": "metric-healthy",
        "warning": "metric-warning",
        "critical": "metric-critical"
    }
    card_class = colors.get(severity, "metric-healthy")
    st.markdown(
        f"""
        <div class="metric-card {card_class}">
            <h3>{title}</h3>
            <h2>{value}</h2>
        </div>
        """, unsafe_allow_html=True
    )

def render_section(title):
    st.markdown(f"### {title}")
    st.markdown("---")

def render_expander(title, content_func, *args, **kwargs):
    with st.expander(title):
        content_func(*args, **kwargs)