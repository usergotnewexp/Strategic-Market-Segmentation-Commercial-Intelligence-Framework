import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.data.mock_generator import MockDataGenerator
from src.services.segmentation import SegmentationService
from src.services.win_loss import WinLossAnalyzer
from src.services.metrics import MetricsCalculator

# Page Config
st.set_page_config(page_title="Schneider Electric Strategic Intelligence", layout="wide", page_icon="⚡")

# Custom CSS for Schneider Branding
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .main-header {
        color: #3dcd58; /* Schneider Green */
        font-weight: 800;
    }
    .kpi-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        border-top: 4px solid #3dcd58;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: bold;
        color: #1f2937;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    generator = MockDataGenerator()
    deals = generator.generate_deals()
    
    segmenter = SegmentationService()
    for deal in deals:
        segmenter.segment_customer(deal.customer)
        
    return deals, segmenter.profiles

deals, profiles = load_data()
analyzer = WinLossAnalyzer(deals)
metrics_calc = MetricsCalculator()

# Header
st.markdown('<h1 class="main-header">⚡ CRM Win/Loss & Segmentation Intelligence</h1>', unsafe_allow_html=True)
st.markdown("Transforming generic positioning into targeted value-driver strategies. Driving **+11% win-rate** and **+₹12Cr+ Revenue**.")
st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Executive Summary",
    "🎯 Segment Intelligence",
    "⚔️ Win/Loss Deep Dive",
    "🎛️ Strategy Simulator",
    "🗃️ Raw Deals DB"
])

# Helpers
def _deals_to_df(deals):
    data = []
    for d in deals:
        data.append({
            "Deal ID": d.deal_id,
            "Segment": d.customer.segment.name if d.customer.segment else "Unknown",
            "Budget (₹)": d.amount,
            "Status": d.status.name,
            "Winner": d.winner.name if d.winner else "None",
            "Loss Reason": d.loss_reason or "N/A"
        })
    return pd.DataFrame(data)

df_deals = _deals_to_df(deals)

# ----------------- TAB 1: EXECUTIVE SUMMARY -----------------

with tab1:
    st.subheader("Business Impact of Segmentation Strategy")
    impact = metrics_calc.calculate_business_impact(38.0, 49.0, 78000.0, 7800)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
            <div class="kpi-card">
                <p>Incremental Revenue (Annual)</p>
                <div class="kpi-value">₹ {impact.total_revenue_opportunity / 10000000:.2f} Cr</div>
                <p style="color:green; font-weight:bold;">▲ +12 Cr Target</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="kpi-card">
                <p>Global Win Rate</p>
                <div class="kpi-value">{impact.win_rate_after}%</div>
                <p style="color:green; font-weight:bold;">▲ +{(impact.win_rate_after - impact.win_rate_before):.1f} pts</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div class="kpi-card">
                <p>Avg Deal Size</p>
                <div class="kpi-value">₹ {impact.avg_deal_size_after:,.0f}</div>
                <p style="color:green; font-weight:bold;">▲ +18% (Better Value)</p>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div class="kpi-card">
                <p>Sales Cycle Time</p>
                <div class="kpi-value">{impact.proposal_cycle_days_after} Days</div>
                <p style="color:green; font-weight:bold;">▼ -29% (Faster Close)</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><hr>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        # Win Rate by Segment Chart
        segment_rates = []
        for p in profiles:
            stats = analyzer.analyze_by_segment(p.segment_type)
            segment_rates.append({"Segment": p.name.split(" (")[0], "Win Rate": stats["win_rate"]})
        
        fig = px.bar(pd.DataFrame(segment_rates), x="Segment", y="Win Rate", color="Segment", 
                     title="Historical Win Rate By Segment", text="Win Rate",
                     color_discrete_sequence=['#3dcd58', '#1f2937', '#9ca3af'])
        fig.update_traces(texttemplate='%{text}%', textposition='outside')
        fig.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', yaxis=dict(showgrid=True, gridcolor='#e5e7eb'))
        fig.add_hline(y=38.0, line_dash="dot", line_color="#ef4444", annotation_text="Old Baseline (38%)")
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Market Share of 100 Deals
        fig2 = px.pie(df_deals, names="Winner", title="Competitive Market Share (Last 100 Deals)", hole=0.4,
                      color_discrete_sequence=['#3dcd58', '#ef4444', '#f59e0b', '#3b82f6'])
        fig2.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig2, use_container_width=True)

# ----------------- TAB 2: SEGMENT INTELLIGENCE -----------------

with tab2:
    st.subheader("Customer Value Drivers by Segment")
    
    selected_segment_name = st.selectbox("Select Segment Profile", [p.name for p in profiles])
    active_profile = next(p for p in profiles if p.name == selected_segment_name)
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.info(f"**Target Audience**: Budget bounds ₹{active_profile.budget_range[0]} - ₹{active_profile.budget_range[1]}")
        st.success(f"**Our Win Strategy**: {active_profile.win_strategy}")
        st.warning(f"**Positioning Statement**: {active_profile.schneider_positioning}")
        
    with col_b:
        # Radar Chart for Value Drivers
        drivers = [d.name.replace("_", " ").title() for d in active_profile.primary_drivers]
        weights = [d.weight * 100 for d in active_profile.primary_drivers]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=weights,
            theta=drivers,
            fill='toself',
            name='Value Importance %',
            line_color='#3dcd58'
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, max(weights)+10])),
            showlegend=False,
            title="What Really Drives Purchase in this Segment?"
        )
        st.plotly_chart(fig_radar, use_container_width=True)

# ----------------- TAB 3: WIN-LOSS DEEP DIVE -----------------

with tab3:
    st.subheader("Why Are We Losing?")
    
    reason_data = []
    for p in profiles:
        reasons = analyzer.get_loss_reasons(p.segment_type)
        for r, count in reasons.items():
            reason_data.append({"Segment": p.name.split(" (")[0], "Loss Reason": r.replace("_", " ").title(), "Count": count})
            
    df_reasons = pd.DataFrame(reason_data)
    
    c3, c4 = st.columns(2)
    with c3:
        if not df_reasons.empty:
            df_reasons = df_reasons.sort_values(by="Count", ascending=True)
            fig_loss = px.bar(df_reasons, y="Loss Reason", x="Count", color="Segment", orientation='h',
                            title="Loss Reasons Distribution",
                            color_discrete_sequence=['#1f2937', '#9ca3af', '#6b7280'])
            fig_loss.update_layout(plot_bgcolor='rgba(0,0,0,0)', xaxis=dict(showgrid=True, gridcolor='#e5e7eb'))
            st.plotly_chart(fig_loss, use_container_width=True)
        else:
            st.info("No loss data available.")
            
    with c4:
        st.markdown("### Competitor Intelligence Matrix")
        strengths = analyzer.aggregate_competitor_strengths()
        for c_enum, desc in strengths.items():
            with st.expander(f"**{c_enum.name}**"):
                st.write(desc)

# ----------------- TAB 4: STRATEGY SIMULATOR -----------------

with tab4:
    st.subheader("🎛️ What-If Strategy Simulator")
    st.write("Adjust our strategic intervention to see the dynamic impact on our pipeline.")
    
    col_sim1, col_sim2 = st.columns(2)
    with col_sim1:
        sim_segment_a = st.slider("Segment A (Small Comm) Target Win Rate %", min_value=10, max_value=80, value=56)
        sim_segment_b = st.slider("Segment B (Industrial) Target Win Rate %", min_value=10, max_value=80, value=62)
        sim_segment_c = st.slider("Segment C (Infrastructure) Target Win Rate %", min_value=10, max_value=80, value=53)
        
    with col_sim2:
        total_leads = st.number_input("Annual Lead Volume", min_value=1000, value=7800, step=100)
        avg_deal_size = st.number_input("Target Average Deal Size (₹)", min_value=50000, value=92000, step=1000)
        
        # Calculate new blended win rate based on leads distribution (35%, 45%, 20%)
        blended_win_rate = (sim_segment_a * 0.35) + (sim_segment_b * 0.45) + (sim_segment_c * 0.20)
        
        sim_impact = metrics_calc.calculate_business_impact(38.0, blended_win_rate, 78000, total_leads)
        sim_rev = (total_leads * (blended_win_rate / 100.0) * avg_deal_size) - (total_leads * 0.38 * 78000)
        
        st.success(f"### Blended Global Win Rate: {blended_win_rate:.1f}%")
        st.info(f"### Simulated Additional Revenue: ₹{sim_rev / 10000000:.2f} Cr / year")

# ----------------- TAB 5: RAW DEALS DB -----------------

with tab5:
    st.subheader("Historical 100 Deals Pipeline")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        f_status = st.multiselect("Filter by Status", df_deals["Status"].unique(), default=df_deals["Status"].unique())
    with col_f2:
        f_winner = st.multiselect("Filter by Winner", df_deals["Winner"].unique(), default=df_deals["Winner"].unique())
        
    filtered_df = df_deals[(df_deals["Status"].isin(f_status)) & (df_deals["Winner"].isin(f_winner))]
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
