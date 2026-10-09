import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="SA Retail Grocery Market Analysis",
    page_icon="🛒",
    layout="wide"
)

# Title & Header
st.title("🛒 South African Grocery Retail Market Share & Stock Performance")
st.markdown("**Author:** Richard Baloyi | *Interactive Retail Intelligence Dashboard*")
st.markdown("---")

# ---------------------------------------------------------
# Sidebar Controls
# ---------------------------------------------------------
st.sidebar.header("Dashboard Controls")
initial_investment = st.sidebar.slider(
    "Initial Investment Amount (R)",
    min_value=1000,
    max_value=100000,
    value=10000,
    step=1000
)

# Calculate investment multiplier relative to R10,000 base
multiplier = initial_investment / 10000.0

# ---------------------------------------------------------
# Row 1 Layout (Graphs 1 & 2)
# ---------------------------------------------------------
col1, col2 = st.columns(2)

# Panel 1: Market Share Historical Trend (2016 - 2024)
with col1:
    st.subheader("1. Grocery Market Share Trends (2016 - 2024)")
    years_1 = [2016, 2018, 2020, 2022, 2024]
    shoprite_1 = [38, 42, 48, 55, 67]
    pnp_1 = [32, 28, 24, 20, 16]

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=years_1, y=shoprite_1, mode='lines+markers+text',
        name='Shoprite/Boxer', text=[f"{v}%" for v in shoprite_1],
        textposition="top center", line=dict(color='#0047AB', width=3.5),
        marker=dict(size=8)
    ))
    fig1.add_trace(go.Scatter(
        x=years_1, y=pnp_1, mode='lines+markers+text',
        name='Pick n Pay', text=[f"{v}%" for v in pnp_1],
        textposition="bottom center", line=dict(color='#E25822', width=3.5),
        marker=dict(size=8)
    ))

    fig1.update_xaxes(title_text="Year", tickvals=years_1)
    fig1.update_yaxes(title_text="Market Share (%)", range=[0, 80])
    fig1.update_layout(height=420, margin=dict(l=20, r=20, t=30, b=20), legend=dict(orientation="h", y=-0.2))
    st.plotly_chart(fig1, use_container_width=True)

# Panel 2: Stock Performance & Compounding Returns
with col2:
    st.subheader("2. Stock Performance Comparison")
    picks = ["Shoprite", "Pick n Pay", "Woolworths", "S&P 500"]
    base_returns = np.array([28500, 4800, 6200, 22000])
    scaled_returns = base_returns * multiplier

    df2 = pd.DataFrame({'Stock Picks': picks, 'Value (R)': scaled_returns})
    fig2 = px.bar(
        df2, x='Stock Picks', y='Value (R)', text='Value (R)',
        color='Stock Picks', color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig2.update_traces(texttemplate='R%{text:,.0f}', textposition='outside')
    fig2.update_yaxes(title_text=f"Value of R{initial_investment:,.0f} Investment")
    fig2.update_layout(height=420, margin=dict(l=20, r=20, t=30, b=20), showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# Row 2 Layout (Graphs 3 & 4)
# ---------------------------------------------------------
col3, col4 = st.columns(2)

# Panel 3: Retail Brand Positioning Map
with col3:
    st.subheader("3. Retail Brand Positioning Map")
    data = {
        'Brand': ['Shoprite', 'Boxer', 'PEP', 'Mr Price', 'Pick n Pay', 'Woolworths', 'Romans', 'Debonairs'],
        'Price Level': [3, 2, 2, 4, 6, 9, 4, 7],
        'Perceived Aspiration': [7, 6, 8, 8, 5, 6, 9, 4],
        'Group': ['Shoprite Group', 'Shoprite Group', 'Value Retail', 'Value Retail', 'Pick n Pay', 'Premium', 'QSR', 'QSR']
    }
    df3 = pd.DataFrame(data)

    fig3 = px.scatter(
        df3, x='Price Level', y='Perceived Aspiration', text='Brand', color='Group',
        color_discrete_sequence=['#0047AB', '#1E90FF', '#FFA500', '#822222']
    )
    fig3.update_traces(marker=dict(size=24, line=dict(width=1.5, color='white')), textposition='top right')

    # Quadrant lines
    fig3.add_vline(x=5.5, line_dash="dash", line_color="gray", opacity=0.6)
    fig3.add_hline(y=5.5, line_dash="dash", line_color="gray", opacity=0.6)

    # Winner Zone Annotation
    fig3.add_annotation(
        x=2.5, y=9.3, text="<b>WINNER ZONE</b><br>(Cheap + Aspirational)",
        showarrow=False, font=dict(color="#0047AB", size=12), align="center"
    )

    fig3.update_xaxes(title_text="Price Level → Cheap to Expensive", range=[0.5, 10.5])
    fig3.update_yaxes(title_text="Perceived Aspiration → Low to High", range=[0.5, 10.5])
    fig3.update_layout(height=450, margin=dict(l=20, r=20, t=30, b=20), legend=dict(orientation="h", y=-0.25))
    st.plotly_chart(fig3, use_container_width=True)

# Panel 4: Market Share Forecast (2025 - 2030)
with col4:
    st.subheader("4. Market Share Forecast (2025 - 2030)")
    years_4 = [2025, 2026, 2027, 2028, 2029, 2030]
    shoprite_4 = [55, 58, 61, 64, 67, 70]
    pnp_4 = [20, 18, 16, 14, 12, 10]
    woolies_4 = [15, 15, 14, 14, 13, 13]

    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(
        x=years_4, y=shoprite_4, mode='lines+markers+text',
        name='Shoprite/Boxer', text=[f"{v}%" for v in shoprite_4],
        textposition="top center", line=dict(color='#0047AB', width=3.5),
        marker=dict(size=8)
    ))
    fig4.add_trace(go.Scatter(
        x=years_4, y=pnp_4, mode='lines+markers+text',
        name='Pick n Pay', text=[f"{v}%" for v in pnp_4],
        textposition="bottom center", line=dict(color='#E25822', width=3.5),
        marker=dict(size=8)
    ))
    fig4.add_trace(go.Scatter(
        x=years_4, y=woolies_4, mode='lines+markers+text',
        name='Woolworths', text=[f"{v}%" for v in woolies_4],
        textposition="bottom center", line=dict(color='#822222', width=3.5),
        marker=dict(size=8)
    ))

    fig4.update_xaxes(title_text="Year", tickvals=years_4)
    fig4.update_yaxes(title_text="Market Share (%)", range=[0, 80])
    fig4.update_layout(height=450, margin=dict(l=20, r=20, t=30, b=20), legend=dict(orientation="h", y=-0.25))
    st.plotly_chart(fig4, use_container_width=True)
