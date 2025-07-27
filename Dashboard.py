import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('TCS_Cleaned_Data (2).csv')
df['Date'] = pd.to_datetime(df['Date'])
df['MA30'] = df['Price'].rolling(window=30).mean()

# Title
st.title("📊 TCS Stock Dashboard (2020–2025)")

# Line chart
fig1 = px.line(df, x='Date', y='Price', title='TCS Stock Price Over Time')
st.plotly_chart(fig1)

# Daily price diff
fig2 = px.bar(df, x='Date', y='Price_diff', title='Daily Price Change')
st.plotly_chart(fig2)

# Moving Average
fig3 = px.line(df, x='Date', y=['Price', 'MA30'], title='Price vs 30-Day Moving Avg')
st.plotly_chart(fig3)

# Range slider
fig4 = px.line(df, x='Date', y='Price', title='Interactive Price Chart')
fig4.update_layout(xaxis_rangeslider_visible=True)
st.plotly_chart(fig4)
