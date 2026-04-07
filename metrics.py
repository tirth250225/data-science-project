import streamlit as st
import numpy as np

def show_metrics(df):
    total_sales = np.sum(df["Sales"])
    total_profit = np.sum(df["Profit"])
    avg_sales = np.mean(df["Sales"])
    total_qty = np.sum(df["Quantity"])

    margin = (total_profit / total_sales) * 100

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Sales", f"{total_sales:,.0f}")
    col2.metric("Total Profit", f"{total_profit:,.2f}")
    col3.metric("Average Sales", f"{avg_sales:,.2f}")
    col4.metric("Quantity Sold", f"{total_qty}")
    col5.metric("Profit Margin", f"{margin:.2f}%")