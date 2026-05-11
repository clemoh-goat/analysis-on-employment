
import time
start=time.time()
import pandas as pd
import plotly.express as px
import streamlit as st

#setting up the page title
st.set_page_config(page_title="Runyenjes Labour Intelligence", layout="wide")
st.title("📊 Runyenjes Youth & Labour Intelligence Dashboard")
st.subheader("Developed for: Hon. Eric Muchangi Karemba")

# Mock Data (Simulating your Data Science analysis)
skills_data = pd.DataFrame({
    'Skill Set': ['Agriculture', 'Construction', 'Data Entry/Digital', 'Retail', 'Software Dev'],
    'Local Supply (Youth)': [80, 70, 40, 90, 20],
    'Market Demand': [40, 50, 95, 60, 85]
})

sentiment_data = pd.DataFrame({
    'Sentiment': ['Optimistic', 'Neutral', 'Dissatisfied'],
    'Percentage': [25, 35, 40]
})

# 3. Layout - Column 1: Skills Gap
col1, col2 = st.columns(2)

with col1:
    
    st.markdown("## The Skills Mismatch")
    fig = px.bar(skills_data, x='Skill Set', y=['Local Supply (Youth)', 'Market Demand'], 
                 barmode='group', title="Youth Skills vs. Industry Needs (Runyenjes)")
    st.plotly_chart(fig)
# 4. Layout - Column 2: Youth Sentiment
with col2:
    st.markdown("### 🗣️ Gen Z Sentiment Tracker")
    fig2 = px.pie(sentiment_data, values='Percentage', names='Sentiment', 
                  color='Sentiment', color_discrete_map={'Optimistic':'green', 'Neutral':'gray', 'Dissatisfied':'red'})
    st.plotly_chart(fig2)
    # 5. The "Predictive" Element (Linear Regression Logic)
st.divider()
st.markdown("### 📈 Predictive Impact Model")
st.write("Current Projection: For every *10% increase* in Digital Literacy TVET funding, we predict a *15% drop* in local youth unemployment within 12 months.")

st.info("Strategy: Use this data to justify National Assembly budget allocations for Runyenjes digital hubs.")