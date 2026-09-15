import os
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EthioChicken Analytics Platform", layout="wide")

@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    master_path = os.path.join(base_dir, 'data', 'processed', 'master_analytics_segmented.csv')
    cluster_path = os.path.join(base_dir, 'data', 'processed', 'agent_cluster_profiles.csv')
    
    if not os.path.exists(master_path):
        master_path = os.path.join(base_dir, '..', 'data', 'processed', 'master_analytics_segmented.csv')
        cluster_path = os.path.join(base_dir, '..', 'data', 'processed', 'agent_cluster_profiles.csv')
        
    master_df = pd.read_csv(master_path)
    cluster_df = pd.read_csv(cluster_path)
    return master_df, cluster_df

df_master, df_clusters = load_data()

# Sidebar Filters
st.sidebar.title("Operational Filters")
selected_region = st.sidebar.selectbox("Select Region", ['All'] + list(df_master['region'].unique()))
selected_tier = st.sidebar.selectbox("Select Agent Tier", ['All'] + list(df_master['agent_tier'].unique()))

filtered_master = df_master.copy()
if selected_region != 'All':
    filtered_master = filtered_master[filtered_master['region'] == selected_region]
if selected_tier != 'All':
    filtered_master = filtered_master[filtered_master['agent_tier'] == selected_tier]

# Main Dashboard Layout
st.title("🐔 EthioChicken Agent Performance & Mortality Analytics")
st.markdown("Portfolio platform monitoring smallholder agent metrics, mortality risk brackets, and regional logistics.")

# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Chicks Ordered", f"{filtered_master['quantity_ordered'].sum():,}")
col2.metric("Avg Mortality Rate", f"{filtered_master['mortality_rate_pct'].mean():.2f}%")
col3.metric("Avg Vaccination Compliance", f"{filtered_master['vaccination_compliance_pct'].mean():.1f}%")
col4.metric("New Tier High-Mortality Rate", f"{(filtered_master[filtered_master['agent_tier']=='New']['mortality_rate_pct'].mean()):.1f}%")

st.markdown("---")

# Visualizations Row 1
c1, c2 = st.columns(2)

with c1:
    st.subheader("Mortality Rate by Agent Tier")
    fig_tier = px.box(
        filtered_master, 
        x='agent_tier', 
        y='mortality_rate_pct', 
        color='agent_tier',
        labels={'agent_tier': 'Agent Tier', 'mortality_rate_pct': 'Mortality Rate (%)'},
        color_discrete_map={'New': '#e74c3c', 'Bronze': '#f39c12', 'Silver': '#3498db', 'Gold': '#2ecc71'}
    )
    fig_tier.add_hline(y=10.0, line_dash="dash", line_color="red", annotation_text="10% Risk Threshold")
    st.plotly_chart(fig_tier, use_container_width=True)

with c2:
    st.subheader("Vaccination Compliance vs Mortality Rate")
    fig_scatter = px.scatter(
        filtered_master, 
        x='vaccination_compliance_pct', 
        y='mortality_rate_pct', 
        color='agent_tier', 
        opacity=0.7,
        labels={'vaccination_compliance_pct': 'Vaccination Compliance (%)', 'mortality_rate_pct': 'Mortality Rate (%)'}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Visualizations Row 2
st.subheader("Agent Performance Segments Distribution")
fig_segments = px.bar(
    filtered_master.groupby(['region', 'segment_name']).size().reset_index(name='agent_count'),
    x='region', 
    y='agent_count', 
    color='segment_name', 
    barmode='group',
    labels={'region': 'Region', 'agent_count': 'Order / Agent Count', 'segment_name': 'Segment'}
)
st.plotly_chart(fig_segments, use_container_width=True)

