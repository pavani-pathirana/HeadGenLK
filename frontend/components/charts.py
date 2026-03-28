import plotly.graph_objects as go


def create_gauge(value: float, title: str, color: str) -> go.Figure:
    """RAM usage gauge for a single model result card."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={"x": [0, 1], "y": [0, 1]},
        title={"text": title, "font": {"size": 12, "color": "#94a3b8"}},
        number={"font": {"color": "#e2e8f0", "size": 18}, "suffix": " MB"},
        gauge={
            "axis": {"range": [None, 500], "tickwidth": 1, "tickcolor": "#475569"},
            "bar":  {"color": color},
            "bgcolor": "rgba(0,0,0,0)",
            "borderwidth": 2,
            "bordercolor": "#475569",
            "steps": [
                {"range": [0,   200], "color": "rgba(96,165,250,0.1)"},
                {"range": [200, 350], "color": "rgba(245,158,11,0.1)"},
                {"range": [350, 500], "color": "rgba(239,68,68,0.1)"},
            ],
        },
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=40, b=20),
        height=160,
    )
    return fig


def create_performance_bar(results: list[dict]) -> go.Figure:
    """Bar chart comparing inference times across models."""
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=[r["name"] for r in results],
        y=[r["inference_time_s"] for r in results],
        marker_color=[r["color"] for r in results],
        text=[f'{r["inference_time_s"]:.2f}s' for r in results],
        textposition="auto",
        textfont={"color": "#e2e8f0", "size": 12},
        name="Inference Time",
    ))
    fig.update_layout(
        title={"text": "Model Performance Comparison", "font": {"color": "#e2e8f0", "size": 16}},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis={"title": "Model",                    "title_font": {"color": "#94a3b8"}, "tickfont": {"color": "#cbd5e1"}},
        yaxis={"title": "Inference Time (seconds)", "title_font": {"color": "#94a3b8"}, "tickfont": {"color": "#cbd5e1"}, "gridcolor": "rgba(148,163,184,0.2)"},
        height=300,
        margin=dict(l=40, r=40, t=50, b=40),
    )
    return fig